import pandas as pd
from datetime import datetime

def agent_admin(message, from_number, df_catalogue):
    """
    Agent Admin - Handles appointments and RDV requests
    Collects information and schedules visits
    """
    
    response = None
    
    # RDV/Visite request
    if any(kw in message for kw in ["visite", "rdv", "rendez-vous", "appointment", "créneau"]):
        response = f"""
📅 RÉSERVATION DE VISITE - ESSALAM

Parfait! Vous souhaitez visiter nos terrains?

✅ Disponibilité: 24h/24 - 7j/7
✅ Types: Terrains R+2, R+1, Fermes oléicoles

Pour confirmer votre RDV, veuillez envoyer:
1️⃣ Votre nom complet
2️⃣ Numéro de téléphone
3️⃣ Type de terrain (R+2, R+1, Ferme)
4️⃣ Créneau préféré

📞 Ou appelez directement: +212 691-897126
⏰ Agent Admin disponible maintenant!

Agence Essalam - وكالة السلام العقارية
        """.strip()
    
    # Dossier/Documentation request
    elif "dossier" in message or "document" in message or "papier" in message:
        response = f"""
📋 DOSSIERS & DOCUMENTATION

Pour constituer votre dossier:
✅ Pièce d'identité
✅ Justificatif de domicile
✅ Attestation de capacité financière
✅ Contrat préalable
✅ Acte de vente

📞 Notre Agent Admin vous guide:
+212 691-897126 / +212 611-715984
Service RDV 24h/24

Agence Essalam - وكالة السلام العقارية
        """.strip()
    
    # Financement/Payment plan
    elif "financement" in message or "paiement" in message or "versement" in message:
        response = f"""
💳 OPTIONS DE PAIEMENT - ESSALAM

✅ Paiement comptant
✅ Versements échelonnés
✅ Financement bancaire
✅ Chèques post-datés
✅ Virement bancaire

📋 Pour obtenir les conditions:
📞 +212 691-897126 (Agent Admin)

Nous proposons des facilités adaptées à votre situation!
Agence Essalam - وكالة السلام العقارية
        """.strip()
    
    # Default admin response
    if not response:
        response = f"""
👨‍💼 AGENT ADMINISTRATIF - ESSALAM

Je peux vous aider pour:
📅 Réserver une visite
📋 Préparer votre dossier
💳 Options de financement
✍️ Signatures de contrats
📞 Suivi de votre dossier

Dites-moi "visite", "dossier" ou "financement"
📞 Contact: +212 691-897126

Agence Essalam - وكالة السلام العقارية
        """.strip()
    
    return response
