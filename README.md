# Alpha-core-nexus-
Agence de marketing digital services 
Je peux vous aider à créer la présentation et une petite application Streamlit pour présenter vos biens (terrains agricoles, fermes fonctionnelles, lots de construction, maisons/immeubles) à Kelaa Sraghna. Ci‑dessous j'ai préparé :

- un README prêt à l'emploi (FR) pour votre dépôt,
- un exemple d'application Streamlit (app.py) qui affiche des annonces et filtre par type/prix/surface,
- un fichier properties.json d'exemple contenant quelques biens.

Je l'ai rédigé pour que vous puissiez copier-coller directement dans votre dépôt. Dites-moi si vous voulez que je le pousse directement dans le repo (j'aurai alors besoin de la confirmation owner/repo — ici je vois marocinvest2016-ai/Alpha-core-nexus- — et l'autorisation d'écrire).

Résumé de ce que j'ai fait et la suite :
- J'ai préparé les fichiers ci-dessous. Vous pouvez les déposer dans votre repo.
- Ensuite, vous pouvez personnaliser les annonces (properties.json) et les images.
- Si vous voulez, je peux aussi créer un formulaire de contact qui envoie des e-mails, intégrer une base de données, ou pousser ces fichiers dans GitHub.

Voici les fichiers prêts à l'emploi.

````markdown name=README.md
# Agence Immobilière — Kelaa Sraghna

Bienvenue sur le dépôt officiel de l'agence immobilière de Kelaa Sraghna. Ce dépôt contient une petite application Streamlit pour présenter et filtrer les biens immobiliers disponibles : terrains agricoles, fermes fonctionnelles, lots de construction, maisons et immeubles.

## Nos services
- Vente de terrains agricoles
- Vente de fermes fonctionnelles (avec infrastructures)
- Vente de lots de construction (zone maison ou immeuble)
- Accompagnement pour visites et formalités administratives
- Estimation et mise en valeur de biens

## Comment utiliser cette application (localement)
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/marocinvest2016-ai/Alpha-core-nexus-.git
   cd Alpha-core-nexus-
   ```
2. Créer un environnement et installer les dépendances :
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows
   pip install -r requirements.txt
   ```
   Exemple de requirements.txt :
   ```
   streamlit
   pandas
   ```
3. Lancer l'application :
   ```bash
   streamlit run app.py
   ```

## Structure proposée
- app.py — application Streamlit pour afficher les annonces
- properties.json — liste des biens (format JSON)
- images/ — dossier pour stocker les images locales (optionnel)

## Personnalisation
- Modifiez `properties.json` pour ajouter/éditer les annonces : titre, type, prix, superficie, description, image_url, contact.
- Vous pouvez remplacer les `image_url` par des chemins locaux `images/nom.jpg`.

## Contact
Agence Immobilière — Kelaa Sraghna  
Téléphone : +212 ...  
Email : contact@votre-agence.ma  

---
Merci — dites-moi si vous voulez que j'ajoute :
- un formulaire de contact (envoi d'e-mails),
- une base de données (SQLite / PostgreSQL),
- l'intégration d'une page web statique ou un déploiement (Streamlit Cloud / Heroku).
``` ````

```python name=app.py
import streamlit as st
import json
import pandas as pd
from urllib.parse import quote

# Chargement des données
def load_properties(path="properties.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

properties = load_properties()

df = pd.DataFrame(properties)

st.set_page_config(page_title="Agence - Kelaa Sraghna", layout="wide")
st.title("Agence Immobilière — Kelaa Sraghna")
st.write("Terrains agricoles, fermes, lots de construction, maisons et immeubles.")

# Sidebar filtres
st.sidebar.header("Filtres")
types = ["Tous"] + sorted(df["type"].unique().tolist())
selected_type = st.sidebar.selectbox("Type de bien", types)
max_price = st.sidebar.number_input("Prix maximum (MAD)", min_value=0, value=int(df["price"].max()))
min_surface = st.sidebar.number_input("Surface min (m²)", min_value=0, value=0)

# Appliquer filtres
filtered = df.copy()
if selected_type != "Tous":
    filtered = filtered[filtered["type"] == selected_type]
filtered = filtered[filtered["price"] <= max_price]
filtered = filtered[filtered["surface"] >= min_surface]

st.sidebar.markdown(f"Biens trouvés : **{len(filtered)}**")

# Affichage des cartes
for _, row in filtered.iterrows():
    cols = st.columns([1, 2])
    with cols[0]:
        if row.get("image_url"):
            st.image(row["image_url"], use_column_width=True)
        else:
            st.write("Aucune image")
    with cols[1]:
        st.subheader(row["title"])
        st.write(f"Type : **{row['type']}**  •  Surface : **{row['surface']} m²**  •  Prix : **{row['price']:,} MAD**")
        st.write(row["description"])
        contact_mail = row.get("contact_email", "contact@votre-agence.ma")
        subject = quote(f"Demande d'information: {row['title']}")
        mailto = f"mailto:{contact_mail}?subject={subject}"
        st.markdown(f"[Contacter]({mailto})  •  Référence : `{row.get('id', '')}`")

st.write("---")
st.write("Pour ajouter ou modifier des biens : éditez le fichier `properties.json` et relancez l'application.")
```

```json name=properties.json
[
  {
    "id": "P-001",
    "title": "Terrain agricole - Haouch Bni",
    "type": "Terrain agricole",
    "price": 250000,
    "surface": 5000,
    "description": "Terrain fertile idéal pour culture maraîchère, proche de l'accès routier principal.",
    "image_url": "https://via.placeholder.com/400x250.png?text=Terrain+agricole",
    "contact_email": "contact@votre-agence.ma"
  },
  {
    "id": "P-002",
    "title": "Ferme fonctionnelle avec hangar",
    "type": "Ferme fonctionnelle",
    "price": 750000,
    "surface": 12000,
    "description": "Ferme équipée, comprenant maison d'habitation, hangar et point d'eau.",
    "image_url": "https://via.placeholder.com/400x250.png?text=Ferme",
    "contact_email": "contact@votre-agence.ma"
  },
  {
    "id": "P-003",
    "title": "Lot de construction - Zone Maison",
    "type": "Lot de construction",
    "price": 120000,
    "surface": 350,
    "description": "Lot bien placé en zone résidentielle, idéal pour maison individuelle ou petit immeuble.",
    "image_url": "https://via.placeholder.com/400x250.png?text=Lot+construction",
    "contact_email": "contact@votre-agence.ma"
  },
  {
    "id": "P-004",
    "title": "Immeuble / Maison à rénover",
    "type": "Maison / Immeuble",
    "price": 420000,
    "surface": 420,
    "description": "Bâtiment sur deux niveaux, possibilité de réhabilitation pour location ou revente.",
    "image_url": "https://via.placeholder.com/400x250.png?text=Maison",
    "contact_email": "contact@votre-agence.ma"
  }
]
```

Remarques et options suivantes :
- Je peux ajouter un fichier requirements.txt et un .gitignore si vous le souhaitez.
- Je peux adapter le texte du README pour une page d'annonce commerciale ou pour Facebook/Avito.
- Je peux pousser ces fichiers dans votre repo si vous confirmez que je peux écrire dans marocinvest2016-ai/Alpha-core-nexus-.

Que voulez-vous que je fasse ensuite ? Voulez-vous :
1) Que je personnalise le contenu (coordonnées, images) maintenant ?  
2) Que je pousse ces fichiers dans le repo (je demanderai confirmation avant d'écrire) ?  
3) Autre (ex. formulaire de contact, déploiement) ?
