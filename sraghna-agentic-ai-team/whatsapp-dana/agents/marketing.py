import pandas as pd

def agent_marketing(message, from_number, df_catalogue):
    """
    Agent Marketing - Responds to multimedia and promotional requests
    Provides videos, images, and marketing content
    """
    
    response = None
    
    # YouTube/Video request
    if "youtube" in message or "video" in message:
        response = f"""
🎬 VISITES VIRTUELLES ESSALAM

Découvrez nos terrains en 360°!
📺 Chaîne YouTube: youtube.com/@Agencekelaa

✨ LOT-R+2-01 Lotissement Essalam
✨ LOT-R+1-02 Quartier Aawatif
🌱 Ferme-OL-01 Zone Agricole Sud

Abonnez-vous pour les dernières vidéos!
📞 Pour visite en direct: +212 691-897126
        """.strip()
    
    # Photo/Catalogue request
    elif "photo" in message or "image" in message or "catalogue" in message:
        response = f"""
📸 CATALOGUE & PHOTOS ESSALAM

Nos photos professionnelles sont disponibles:
✅ Plans aériens drone
✅ Photos des terrains
✅ Plans d'aménagement
✅ Vidéos 360°

📧 Envoyez "catalogue" pour reçevoir le PDF complet
📞 +212 691-897126 ou +212 611-715984
Agence Essalam - وكالة السلام العقارية
        """.strip()
    
    # Story/Content creation
    elif "post" in message or "story" in message or "promotion" in message:
        response = f"""
📱 NOUVEAU LOT R+2 DISPONIBLE!

🔥 LOT R+2 DISPO - ESSALAM 🔥
📍 Lotissement Essalam, près Aawatif 2
📐 200 m² | Constructible R+2
💰 700,000 DH | 3,500 DH/m²

Visite 24/7 : +212 691-897126
Agence Essalam - وكالة السلام العقارية

#ImmobilierKelaa #TerrainABatir #AgenceEssalam
        """.strip()
    
    # Default marketing response
    if not response:
        response = f"""
📢 SERVICE MARKETING ESSALAM

Nous pouvons vous fournir:
✅ Photos professionnelles
✅ Vidéos drone 360°
✅ Plans d'aménagement
✅ Catalogues numériques
✅ Posts réseaux sociaux

📞 Demandez nos contenus: +212 691-897126
Agence Essalam - وكالة السلام العقارية
        """.strip()
    
    return response
