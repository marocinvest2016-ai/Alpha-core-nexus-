# DANA WhatsApp Automation - Guide de Déploiement 🚀

## Vue d'ensemble

Ce webhook Python Flask connecte DANA (notre système IA) à WhatsApp Business API pour répondre automatiquement 24/7 aux requêtes immobilières.

**Flux:**
```
Client WhatsApp → WhatsApp Business API → Webhook Flask → DANA Agents → Réponse Auto
```

---

## 📋 Prérequis

1. **Compte Meta Business** (Facebook)
2. **Numéro WhatsApp Business**: +212 691-897126
3. **Token WhatsApp**: Depuis developers.facebook.com
4. **Serveur Cloud** (Render, Railway, Heroku, ou VPS)
5. **Python 3.8+** et pip

---

## 🔧 Installation Locale

### 1. Cloner le repo et naviguer
```bash
git clone https://github.com/marocinvest2016-ai/Alpha-core-nexus-.git
cd Alpha-core-nexus-/sraghna-agentic-ai-team/whatsapp-dana
```

### 2. Créer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement
```bash
cp .env.example .env
# Éditer .env avec tes credentials
```

Remplir `.env`:
```env
WHATSAPP_TOKEN=your_token_from_meta
PHONE_NUMBER_ID=your_phone_number_id
VERIFY_TOKEN=your_custom_verify_token
PORT=5000
```

### 5. Tester localement
```bash
python app.py
```

Le serveur sera accessible à: `http://localhost:5000`

---

## 🧪 Test du Webhook Localement

### Test 1: Health Check
```bash
curl http://localhost:5000/health
```

Réponse attendue:
```json
{"status": "healthy", "timestamp": "2026-08-04T..."}
```

### Test 2: Consulter le catalogue
```bash
curl http://localhost:5000/catalogue
```

### Test 3: Simuler un message WhatsApp
```bash
curl -X POST http://localhost:5000/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "entry": [{
      "changes": [{
        "value": {
          "messages": [{
            "from": "212691234567",
            "type": "text",
            "text": {"body": "Quel est le prix des terrains R+2 à Essalam?"}
          }]
        }
      }]
    }]
  }'
```

---

## 📱 Configuration WhatsApp Business API

### Étape 1: Créer l'App Meta
1. Va sur [developers.facebook.com](https://developers.facebook.com/)
2. Crée une nouvelle App (type: Business)
3. Ajoute le produit "WhatsApp"

### Étape 2: Obtenir les Credentials
1. **PHONE_NUMBER_ID**: Dans "Phone Numbers" → Copie l'ID
2. **WHATSAPP_TOKEN**: Dans "System User" → Génère un token permanent
3. **VERIFY_TOKEN**: Crée toi-même une chaîne random (ex: `dana_webhook_2026`)

### Étape 3: Configurer le Webhook

#### Sur Meta Dashboard:
1. Vas dans **Settings → Webhooks**
2. **Callback URL**: `https://ton-domaine.com/webhook` (après deploy)
3. **Verify Token**: Le token que tu as créé
4. **Subscribe to Fields**: `messages`, `message_status`
5. Clique **Subscribe**

#### Valider le Webhook:
```bash
curl -X GET "http://localhost:5000/webhook?hub.verify_token=dana_webhook_2026&hub.challenge=test_challenge_value"
```

---

## 🚀 Déploiement en Production

### Option A: Render.com (Recommandé - Gratuit)

1. **Créer un compte** sur [render.com](https://render.com/)
2. **New → Web Service**
3. Connecter ton repo GitHub
4. **Configuration:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Environment Variables:
     ```
     WHATSAPP_TOKEN=ton_token
     PHONE_NUMBER_ID=ton_id
     VERIFY_TOKEN=dana_webhook_2026
     PORT=5000
     ```
5. **Deploy** → Ton URL sera `https://dana-whatsapp.onrender.com`

### Option B: Railway.app

1. Créer un compte sur [railway.app](https://railway.app/)
2. Connecter GitHub et déployer
3. Configurer les env vars
4. Ajouter `Procfile`:
   ```
   web: gunicorn app:app
   ```

### Option C: Heroku (avec plan payant)

1. `heroku create dana-whatsapp`
2. `heroku config:set WHATSAPP_TOKEN=xxx`
3. `git push heroku main`

### Option D: VPS Propre (AWS, DigitalOcean, OVH)

```bash
# Sur le serveur:
sudo apt update && sudo apt install python3-pip
git clone repo.git
cd whatsapp-dana
pip install -r requirements.txt
python app.py  # Ou via systemd/supervisor
```

---

## 🔗 Connecter à WhatsApp Business

### Après déploiement:

1. **Copie ton URL publique** (ex: `https://dana-whatsapp.onrender.com`)
2. **Meta Dashboard → Settings → Webhooks:**
   - Callback URL: `https://dana-whatsapp.onrender.com/webhook`
   - Verify Token: `dana_webhook_2026`
3. **Test la connexion**:
   ```bash
   curl -X GET "https://dana-whatsapp.onrender.com/webhook?hub.verify_token=dana_webhook_2026&hub.challenge=test"
   ```
   → Doit retourner `test`

4. **Envoie un message WhatsApp** à +212 691-897126:
   ```
   Quel est le prix des terrains R+2 à Essalam?
   ```
   → DANA doit répondre en < 5s

---

## 🧠 Architecture DANA Agents

### Agent Ventes (`agents/ventes.py`)
- Mots-clés: "prix", "terrain", "r+2", "r+1", "essalam"
- Retourne: Prix, superficie, description, contact

### Agent Marketing (`agents/marketing.py`)
- Mots-clés: "video", "youtube", "photo", "catalogue"
- Retourne: Liens vidéo, catalogues, posts promo

### Agent Admin (`agents/admin.py`)
- Mots-clés: "visite", "rdv", "rendez-vous", "dossier"
- Retourne: Formulaire RDV, instructions dossier, options financement

### Agent Analyse (`agents/analyse.py`)
- Mots-clés: "prix m²", "comparaison", "tendance", "marché"
- Retourne: Analyses prix, comparaisons, recommandations

---

## 📊 Monitoring & Logs

### Sur Render/Railway:
- **Logs en temps réel**: Dashboard → Logs
- **Health Check**: `curl https://ton-app.onrender.com/health`

### Logs locaux:
```bash
tail -f app.log  # Si tu redirige les logs
```

---

## 🐛 Troubleshooting

### "Webhook not responding"
→ Vérifie VERIFY_TOKEN, check les logs du serveur

### "Catalogue not loading"
→ Vérifie le chemin CSV, make sure fichier existe sur `main`

### "Messages not sending"
→ Vérifie TOKEN et PHONE_NUMBER_ID, test avec curl

### "500 Internal Server Error"
→ Regarde les logs, check les exceptions Python

---

## 📞 Support

- **Contact Agence**: +212 691-897126
- **WhatsApp Business**: +212 691-897126
- **GitHub Issues**: Report bugs sur le repo

---

## ✅ Checklist Final

- [ ] Env vars configurées (TOKEN, PHONE_ID, VERIFY_TOKEN)
- [ ] Tests locaux réussis (health, catalogue, message simulation)
- [ ] App déployée sur Render/Railway/VPS
- [ ] Webhook URL configurée dans Meta Dashboard
- [ ] Webhook validation réussie (GET request retourne challenge)
- [ ] Message test envoyé via WhatsApp → Réponse DANA reçue
- [ ] Agent Ventes répond aux "prix terrain R+2 Essalam" ✓
- [ ] Agent Admin gère les "visite" et "rdv" ✓
- [ ] Logs monitoring en place ✓

**Tu es prêt pour DANA 24/7 en production! 🎉📲**
