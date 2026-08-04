import pandas as pd

def agent_analyse(message, from_number, df_catalogue):
    """
    Agent Analyse - Provides market analysis and price comparisons
    Analyzes price per m² by location and type
    """
    
    if df_catalogue is None or df_catalogue.empty:
        return "❌ Données d'analyse indisponibles. Contactez +212 691-897126"
    
    response = None
    
    # Prix m² by location
    if "prix m2" in message or "m² aawatif" in message:
        try:
            aawatif = df_catalogue[df_catalogue['localisation'] == 'Quartier Aawatif'].iloc[0]
            response = f"""
📊 ANALYSE PRIX - QUARTIER AAWATIF

Localisation: Quartier Aawatif
📐 Prix/m²: {int(aawatif['prix_par_m2'])} DH/m²
🏗️ Type: R+1 Constructible
📏 Superficie disponible: {int(aawatif['superficie_m2'])} m²
💰 Total: {int(aawatif['superficie_m2'] * aawatif['prix_par_m2']):,} DH

Comparaison Essalam:
• R+2 Lotissement: 3,500 DH/m²
• R+1 Aawatif: 3,400 DH/m² ✨ Plus avantageux
• Agricole: 50 DH/m²

📞 Infos détaillées: +212 691-897126
            """.strip()
        except Exception as e:
            response = f"❌ Erreur analyse Aawatif: {str(e)}"
    
    # Comparaison R+2 vs R+1
    elif "comparaison" in message or "r+2 vs r+1" in message:
        response = f"""
📊 ANALYSE COMPARATIVE - ESSALAM

🔴 LOT R+2 (Lotissement Essalam)
  • Superficie: 200 m²
  • Prix/m²: 3,500 DH
  • Total: 700,000 DH
  • Avantage: Plus proche route principale

🟢 LOT R+1 (Quartier Aawatif)
  • Superficie: 250 m²
  • Prix/m²: 3,400 DH
  • Total: 850,000 DH
  • Avantage: Plus spacieux, eau/électricité proche

🌱 FERME OLÉICOLE
  • Superficie: 5,000 m²
  • Prix/m²: 50 DH
  • Total: 250,000 DH
  • Avantage: Investissement agricole, clé en main

💡 Conseil: Selon votre budget et projet!
📞 Analyse personnalisée: +212 691-897126
        """.strip()
    
    # Tendance marché
    elif "tendance" in message or "marché" in message or "évolution" in message:
        response = f"""
📈 TENDANCE MARCHÉ - KELAÂ SRAGHNA 2026

✅ Demande: En hausse (+15% YoY)
✅ Disponibilité: Limitée (terrains prime)
✅ Prix: Stables, légers ajustements
✅ Secteur: Lotissement Essalam très demandé

FACTEURS POSITIFS:
✨ Infrastructure routière améliorée
✨ Croissance démographique
✨ Zone commerciale proche
✨ Services 24h/24

💼 Investissement recommandé: OUI
📞 Stratégie personnalisée: +212 691-897126
        """.strip()
    
    # Default analysis response
    if not response:
        response = f"""
📊 AGENT ANALYSE - ESSALAM

Je fournis l'analyse sur:
💹 Prix/m² par quartier
📈 Comparaisons terrains
🔍 Tendance marché
💡 Recommandations
💰 ROI investissement

Demandez l'analyse que vous souhaitez!
📞 +212 691-897126 - Agent Analyse

Agence Essalam - وكالة السلام العقارية
        """.strip()
    
    return response
