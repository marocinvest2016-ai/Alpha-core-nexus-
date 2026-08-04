import pandas as pd
from datetime import datetime

def agent_ventes(message, from_number, df_catalogue):
    """
    Agent Ventes - Responds to price and availability queries
    Searches catalogue_terrains.csv for matching lots
    """
    
    if df_catalogue is None or df_catalogue.empty:
        return "❌ Catalogue indisponible. Veuillez contacter +212 691-897126"
    
    # Search logic
    response = None
    
    # R+2 query
    if "r+2" in message and ("essalam" in message or "prix" in message):
        try:
            matching = df_catalogue[df_catalogue['reference'] == 'LOT-R+2-01']
            if matching.empty:
                response = "❌ LOT-R+2-01 not found in catalogue"
            else:
                lot = matching.iloc[0]
                total_prix = int(lot['superficie_m2'] * lot['prix_par_m2'])
                response = f"""
🔥 LOT R+2 DISPONIBLE

Réf: {lot['reference']}
📍 {lot['localisation']}
📐 Superficie: {int(lot['superficie_m2'])} m²
🏗️ Constructible: R+2
💰 Prix: {int(lot['prix_par_m2'])} DH/m² → TOTAL: {total_prix:,} DH
📝 Détails: {lot['description']}
✅ Statut: {lot['status']}

📞 Contact: {lot['contact']}
Agence Essalam - Service 24h/24
Visites virtuelles: youtube.com/@Agencekelaa
                """.strip()
        except Exception as e:
            response = f"❌ Erreur recherche LOT-R+2-01: {str(e)}"
    
    # R+1 query
    elif "r+1" in message and "essalam" in message:
        try:
            matching = df_catalogue[df_catalogue['reference'] == 'LOT-R+1-02']
            if matching.empty:
                response = "❌ LOT-R+1-02 not found in catalogue"
            else:
                lot = matching.iloc[0]
                total_prix = int(lot['superficie_m2'] * lot['prix_par_m2'])
                response = f"""
🏠 LOT R+1 DISPONIBLE

Réf: {lot['reference']}
📍 {lot['localisation']}
📐 Superficie: {int(lot['superficie_m2'])} m²
🏗️ Constructible: R+1
💰 Prix: {int(lot['prix_par_m2'])} DH/m² → TOTAL: {total_prix:,} DH
📝 Détails: {lot['description']}
✅ Statut: {lot['status']}

📞 Contact: {lot['contact']}
Agence Essalam - Service 24h/24
                """.strip()
        except Exception as e:
            response = f"❌ Erreur recherche LOT-R+1-02: {str(e)}"
    
    # Ferme query
    elif "ferme" in message or "agricole" in message:
        try:
            matching = df_catalogue[df_catalogue['reference'] == 'Ferme-OL-01']
            if matching.empty:
                response = "❌ Ferme-OL-01 not found in catalogue"
            else:
                lot = matching.iloc[0]
                total_prix = int(lot['superficie_m2'] * lot['prix_par_m2'])
                response = f"""
🌳 FERME OLÉICOLE DISPONIBLE

Réf: {lot['reference']}
📍 {lot['localisation']}
📐 Superficie: {int(lot['superficie_m2'])} m²
🌳 Type: Ferme oléicole clé en main
💰 Prix: {int(lot['prix_par_m2'])} DH/m² → TOTAL: {total_prix:,} DH
📝 Détails: {lot['description']}
✅ Statut: {lot['status']}

📞 Contact: {lot['contact']}
Agence Essalam - Service 24h/24
                """.strip()
        except Exception as e:
            response = f"❌ Erreur recherche ferme: {str(e)}"
    
    # General price inquiry
    elif "prix" in message:
        try:
            response = f"""
💰 PRIX ESSALAM - Catalogue Actuel:

✨ LOT-R+2-01: 200m² × 3500 DH/m² = 700,000 DH
✨ LOT-R+1-02: 250m² × 3400 DH/m² = 850,000 DH
🌳 Ferme-OL-01: 5000m² × 50 DH/m² = 250,000 DH

📞 Infos détaillées: +212 691-897126
Visites 24h/24 - Agence Essalam
            """.strip()
        except Exception as e:
            response = f"❌ Erreur lors de la lecture du catalogue: {str(e)}"
    
    # Default response
    if not response:
        response = f"""
👋 Bienvenue chez Agence Essalam!

Vous pouvez me demander:
💬 "Quel est le prix des terrains R+2 à Essalam?"
💬 "J'ai besoin d'un terrain R+1"
💬 "Infos sur les fermes"
💬 "Je veux une visite"

📞 Contact direct: +212 691-897126
Service 24h/24 - وكالة السلام العقارية
        """.strip()
    
    return response
