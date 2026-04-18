
# 🧬 Face Embedding & Comparison API (InsightFace + FastAPI)

Une solution robuste et performante pour la génération d'**embeddings faciaux** et la **comparaison biométrique**, basée sur **InsightFace** et exposée via une interface **FastAPI**.

Ce microservice transforme des visages en vecteurs numériques (512 dimensions) permettant d'identifier, comparer et authentifier des individus avec une précision de pointe.

---

## 🚀 Fonctionnalités

* 🔹 **Extraction d’embedding (Simple) :** Génère un vecteur pour une image contenant exactement un visage.
* 🔹 **Extraction d’embeddings (Multiple) :** Détecte et vectorise tous les visages présents sur une image.
* 🔹 **Comparaison de Vecteurs :** Calcule la similarité cosinus entre deux embeddings pour vérifier l'identité.
* 🔹 **Comparaison d'Images (Directe) :** Pipeline complet prenant deux photos pour retourner un score de correspondance et une décision (True/False).
* 🔹 **Optimisation CPU :** Inférence ultra-rapide via **ONNX Runtime**, configurée pour fonctionner sans GPU (idéal pour le cloud standard).
* 🔹 **Validation Intelligente :** Vérification stricte des formats d'image et du nombre de visages détectés.
* 🔹 **Architecture Modulaire :** Design basé sur des services et un pattern Singleton pour une gestion efficace de la mémoire.

---

## 🧠 Technologies Utilisées

* **Python 3.13+**
* **FastAPI** (Framework web haute performance)
* **InsightFace** (Modèle Buffalo_L de pointe)
* **ONNX Runtime** (Moteur d'inférence optimisé CPU)
* **NumPy** (Calculs vectoriels pour la similarité)
* **OpenCV** (Traitement d'images)

---

## 📁 Structure du Projet

```text
.
├── app/
│   ├── main.py              # Points d'entrée de l'API (Endpoints)
│   ├── core/
│   │   └── model_config.py  # Configuration Singleton du modèle
│   └── services/
│       ├── embedding_service.py   # Logique d'extraction des vecteurs
│       └── comparison_service.py  # Logique de similarité cosinus
├── models/
│   └── buffalo_l/           # Fichiers ONNX du modèle
├── Dockerfile               # Conteneurisation optimisée
├── requirements.txt         # Dépendances du projet
└── README.md
```

---

## ⚙️ Installation & Lancement

### 1. Installation Locale
```bash
# Cloner le projet
git clone [https://github.com/Mawule1405/face_embedding_api.git](https://github.com/Mawule1405/face_embedding_api.git)
cd face_embedding_api

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'API
uvicorn app.main:app --reload
```

### 2. Utilisation avec Docker
```bash
# Build de l'image
docker build -t face-embedding-api .

# Lancement du conteneur
docker run -p 8000:8000 face-embedding-api
```

📍 **API accessible sur :** `http://localhost:8000`  
📚 **Documentation Swagger :** `http://localhost:8000/docs`

---

## 🛠 Endpoints principaux

### 1. Embedding (Image unique)
**POST** `/embedding_one_face_image`  
Génère l'embedding pour une image contenant **strictement un seul visage**.

### 2. Embeddings multiples
**POST** `/embedding_multiple_face_image`  
Retourne une liste d'embeddings pour **tous les visages** détectés sur l'image.

### 3. Comparaison de Vecteurs
**POST** `/compare_vectors`  
Prend deux listes de flottants (embeddings) en entrée et retourne le score de similarité.
* **Score > 0.4 :** Probablement la même personne.

### 4. Comparaison d'Images
**POST** `/compare_images`  
Envoi de deux fichiers images. L'API extrait les visages les plus saillants et compare leur identité.

---

## 💡 Bonnes Pratiques & Notes

* ✔️ **Normalisation :** Les embeddings sont normalisés pour une utilisation directe avec la similarité cosinus.
* ✔️ **Performance :** Le modèle `buffalo_l` est chargé une seule fois au démarrage pour optimiser les temps de réponse.
* ⚠️ **Note Windows/WSL2 :** L'API est forcée sur CPU (`ctx_id=-1`) pour garantir la compatibilité sans configuration GPU complexe.

---

## 🎯 Cas d'Utilisation

* 🆔 **Authentification Biométrique**
* 🕒 **Systèmes de Pointage (Attendance)**
* 🔍 **Détection de Doublons dans des bases de données**
* 🛡️ **Sécurité et Surveillance Intelligente**

---

## 👤 Auteur
**HELOU Komlan Mawulé (Taurus)** Ingénieur de Conception en Informatique & Développeur Freelance.  
*Expertise en intégration d'IA et automatisation logicielle.*

---

## 📄 Licence
Ce projet est sous licence **MIT**.
