#  Face Embedding API (InsightFace + FastAPI)

Une API performante de génération d’**embeddings faciaux** basée sur **InsightFace** et exposée via **FastAPI**.
Ce service permet de transformer une image contenant un ou plusieurs visages en vecteurs numériques exploitables pour des systèmes de reconnaissance faciale.

---

##  Fonctionnalités

* 🔹 Extraction d’embedding pour **une seule personne**
* 🔹 Extraction d’embeddings pour **plusieurs visages**
* 🔹 Validation des fichiers image
* 🔹 Normalisation des embeddings (optimisée pour la similarité cosinus)
* 🔹 Architecture modulaire (services + config)
* 🔹 Prêt pour conteneurisation avec Docker

---

## 🧠 Technologies utilisées

* Python 3.13.3
* FastAPI
* InsightFace
* OpenCV
* NumPy
* ONNX Runtime

---

## 📁 Structure du projet

```
.
├── app/
│   ├── main.py
│   ├── core/
│   │   └── model_config.py
│   ├── services/
│   │   └── embedding_service.py
│
├── models/
|   |__buffalo_l/         # Modèle InsightFace (ONNX)
|   |__buffalo_l.zip
├── Dockerfile
├── requirements.txt
└── README.md
└── license

```

---

##  Installation

### 1. Cloner le projet

```bash
git clone <repo_url>
cd project
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## ▶️ Lancer l’application

```bash
uvicorn app.main:app --reload
```

📍 API disponible sur :
http://localhost:8000

📚 Documentation interactive :
http://localhost:8000/docs

---

##  Endpoints

###  1. Embedding (1 seul visage)

**POST** `/embedding_one_face_image`

Génère un embedding pour une image contenant **exactement un visage**

#### Contraintes :

* Format : png, jpg, jpeg, webp
* Refuse :

  * aucune face
  * plusieurs faces

#### Réponse :

```json
{
  "embedding": [0.123, -0.456, ...],
  "dimension": 512
}
```

---

###  2. Embeddings multiples

**POST** `/embedding_multiple_face_image`

 Génère des embeddings pour **tous les visages détectés**

#### Réponse :

```json
{
  "nb_faces": 2,
  "embeddings": [
    [...],
    [...]
  ]
}
```

---

##  Dockerisation

### Build

```bash
docker build -t face-embedding-api .
```

### Run

```bash
docker run -p 8000:8000 face-embedding-api
```

---

##  Modèle utilisé

Le projet utilise le modèle **buffalo_l** de InsightFace :

* Détection de visage
* Alignement
* Extraction d’embedding

Les fichiers ONNX doivent être placés dans :

```
/root/.insightface/models/buffalo_l/
```

---

##  Bonnes pratiques

* ✔️ Normalisation des embeddings avant comparaison
* ✔️ Validation stricte des entrées
* ✔️ Gestion des erreurs HTTP
* ✔️ Chargement unique du modèle (singleton)

---

> ⚠️ **Note for Windows/WSL2 users:** > This API is configured to run on **CPU** (ctx_id=-1) to ensure compatibility across machines without dedicated GPUs.

##  Cas d’utilisation

* Système de pointage (attendance)
* Reconnaissance faciale
* Détection d’inconnus
* Authentification biométrique
* Surveillance intelligente

---

##  Améliorations possibles

* Endpoint de comparaison (`/compare`)
* Intégration base de données (PostgreSQL)
* Gestion des utilisateurs
* Détection automatique des inconnus
* Déploiement cloud (AWS, GCP)

---



##  Auteur

Projet développé par HELOU Komlan Mawulé (Taurus) dans le cadre d’un système avancé de reconnaissance faciale et d’intelligence artificielle.

---

##  Licence

MIT License
