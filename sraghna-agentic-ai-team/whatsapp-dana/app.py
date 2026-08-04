from flask import Flask, request, jsonify
import pandas as pd
import requests
import os
from dotenv import load_dotenv
import json
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration - Dynamic CSV path (works local + prod)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "data", "immobilier", "catalogue_terrains.csv")

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

# Import DANA agents
from agents.ventes import agent_ventes
from agents.marketing import agent_marketing
from agents.admin import agent_admin
from agents.analyse import agent_analyse

# Load catalogue once at startup
try:
    df_catalogue = pd.read_csv(CSV_PATH)
    print(f"✅ Catalogue loaded from: {CSV_PATH}")
except Exception as e:
    print(f"⚠️ Error loading CSV: {e}")
    print(f"Looking for: {CSV_PATH}")
    df_catalogue = None


@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    """Main webhook endpoint for WhatsApp Business API"""
    
    if request.method == "GET":
        # Webhook verification
        verify_token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        
        if verify_token == VERIFY_TOKEN:
            return challenge
        else:
            return "Invalid verify token", 403
    
    elif request.method == "POST":
        try:
            data = request.get_json()
            
            # Extract message details
            if "entry" not in data or not data["entry"]:
                return jsonify({"status": "ok"}), 200
            
            entry = data["entry"][0]
            if "changes" not in entry or not entry["changes"]:
                return jsonify({"status": "ok"}), 200
            
            changes = entry["changes"][0]
            if "value" not in changes or "messages" not in changes["value"]:
                return jsonify({"status": "ok"}), 200
            
            message_data = changes["value"]["messages"][0]
            from_number = message_data["from"]
            message_type = message_data["type"]
            
            # Process text messages
            if message_type == "text":
                message_text = message_data["text"]["body"].lower()
                
                # Route to appropriate agent
                response = route_message(message_text, from_number, df_catalogue)
                
                if response:
                    send_whatsapp_message(from_number, response)
            
            return jsonify({"status": "received"}), 200
        
        except Exception as e:
            print(f"❌ Error processing webhook: {e}")
            return jsonify({"error": str(e)}), 500


def route_message(message, from_number, df):
    """
    Route message to appropriate DANA agent based on keywords
    """
    
    # Keywords mapping
    keywords = {
        "ventes": ["prix", "terrain", "r+2", "r+1", "ferme", "coût", "disponible", "essalam"],
        "rdv": ["visite", "rdv", "rendez-vous", "appointment", "quand", "créneau"],
        "marketing": ["photo", "video", "youtube", "image", "catalogue"],
        "analyse": ["analyse", "m²", "comparaison", "prix m2", "moyenne", "quartier"]
    }
    
    # Determine agent
    agent_type = "ventes"  # default
    
    if any(kw in message for kw in keywords["rdv"]):
        agent_type = "rdv"
    elif any(kw in message for kw in keywords["marketing"]):
        agent_type = "marketing"
    elif any(kw in message for kw in keywords["analyse"]):
        agent_type = "analyse"
    
    # Execute appropriate agent
    if agent_type == "rdv":
        return agent_admin(message, from_number, df)
    elif agent_type == "marketing":
        return agent_marketing(message, from_number, df)
    elif agent_type == "analyse":
        return agent_analyse(message, from_number, df)
    else:
        return agent_ventes(message, from_number, df)


def send_whatsapp_message(to_number, text):
    """
    Send message via WhatsApp Business API
    """
    url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
    
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "text",
        "text": {
            "body": text
        }
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"✅ Message sent to {to_number}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error sending message: {e}")


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()}), 200


@app.route("/catalogue", methods=["GET"])
def get_catalogue():
    """Endpoint to retrieve current catalogue (for debugging)"""
    if df_catalogue is not None:
        return jsonify(df_catalogue.to_dict(orient="records")), 200
    return jsonify({"error": "Catalogue not loaded"}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, port=port)
