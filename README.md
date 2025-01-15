# FastAPI Cas Pratique : Génération et extraction d'informations à l'aide des LLMs

## Introduction

Dans un monde où les technologies de l’intelligence artificielle (IA) se démocratisent rapidement, les modèles de langage de grande envergure (LLM) occupent une place cruciale dans l'automatisation et l'optimisation des processus métiers. Ces modèles, soutenus par des infrastructures puissantes, permettent de résoudre des problématiques complexes, notamment la génération de contenu et l'extraction structurée d'informations.

Ce projet s’inscrit dans cette dynamique en proposant une solution novatrice basée sur **FastAPI** et un **modèle LLM fourni par Scaleway**. L’objectif est double :  
- **Générer automatiquement des transcripts d'appels** entre clients et agents en fonction d’un sujet donné.  
- **Extraire des informations spécifiques** à partir de ces transcripts grâce à des requêtes formulées librement par l’utilisateur.  


---

## Objectifs du Projet

1. Développer une **API** capable de générer des transcripts réalistes d’appels entre clients et agents de centre de contact.
2. Proposer une fonctionnalité d’**extraction d’informations** flexible et précise à partir de ces transcripts.

---

## Prérequis

Avant de commencer, assurez-vous que votre système remplit les conditions suivantes :

- **Python 3.8** ou supérieur
- **Un compte Scaleway AI** avec une clé API active

## Installation et Configuration


### Étape 1 : Cloner le dépôt Git
#### Clonez le dépôt du projet à l’aide de la commande suivante dans votre terminal :

git clone https://github.com/ghaileneboughzala/FastAPI-Case-Practice.git

cd FastAPI-Case-Practice

### Étape 2 : Créer un environnement virtuel
#### Créez un environnement virtuel Python pour isoler les dépendances :
python -m venv venv

#### Activez l’environnement virtuel :

##### Sur Linux/macOS :
source venv/bin/activate

##### Sur Windows :
venv\Scripts\activate

### Étape 3 : Installer les dépendances
#### Installez toutes les bibliothèques nécessaires au projet à l’aide de la commande suivante :

pip install fastapi uvicorn pydantic requests python-dotenv streamlit pytest

## Exécution du Projet
### Lancer le serveur FastAPI
#### 1. Pour démarrer le backend et accéder à l’API, exécutez la commande suivante :
uvicorn main:app --reload
#### 2. Le serveur sera lancé sur l’adresse suivante :
http://127.0.0.1:8000/docs

### Lancer l'interface utilisateur avec Streamlit
### Une interface simple et interactive a été créée avec Streamlit. 
#### 1. Exécutez la commande suivante pour lancer Streamlit :
streamlit run app.py
#### 2. Une fois le serveur Streamlit démarré, accédez à l’interface utilisateur dans votre navigateur à l’adresse :
http://localhost:8501

## Structure du Projet

- **fastAPImain.py** : Contient l'implémentation avec **FastAPI**.
- **main.py** : Contient l'implémentation avec **Streamlit**.
- **.env** : Fichier de configuration pour stocker la clé API Scaleway de manière sécurisée.


---
## Stack Technique

### 1. FastAPI
Framework web Python rapide et moderne, conçu pour créer des APIs performantes et documentées.

- **Dépendances nécessaires** :  
  - Python 3.7+  
  - FastAPI  
  - Uvicorn (serveur ASGI)  

- **Caractéristiques principales** :  
  - Documentation interactive intégrée avec **Swagger** et **ReDoc**.  
  - Validation et sérialisation des données grâce à **Pydantic**.  
  - Compatibilité avec **Starlette** pour des performances optimales.

### 2. Pydantic
Bibliothèque utilisée pour la validation et la sérialisation des données.

- **Dépendances nécessaires** :  
  - Python 3.6+  
  - Pydantic (`pip install pydantic`)  

- **Caractéristiques principales** :  
  - Définition stricte des modèles de données.  
  - Génération automatique d’erreurs détaillées en cas de non-conformité.  
  - Utilisation pour valider les requêtes API.

### 3. Requests
Bibliothèque Python élégante pour gérer les requêtes HTTP.

- **Caractéristiques principales** :  
  - Support complet des méthodes HTTP standard.  
  - Gestion des sessions et des cookies.  
  - Simplifie l’intégration avec des APIs tierces.

### 4. Scaleway
Plateforme cloud française offrant des services d’IA, dont des modèles LLM performants.

- **Dépendances nécessaires** :  
  - Création d’un compte Scaleway.  
  - Génération d’une clé API.  

- **Caractéristiques principales** :  
  - Fournit des services d’inférence IA compatibles avec les standards OpenAI.  
  - Accès gratuit en phase bêta pour des tests et des prototypes.  

- **Avantages pour ce projet** :  
  - API standardisée pour une intégration rapide.  
  - Réduction des coûts grâce à l’accès gratuit.

### 5. Modèle LLM : Mistral Nemo Instruct 2407
Modèle optimisé pour des tâches d’instruction et des réponses structurées.

- **Caractéristiques principales** :  
  - Génération de contenu contextuellement pertinent.  
  - Paramètres ajustables (`max_tokens`, `temperature`, `top_p`).  
  - Hébergé sur Scaleway pour une intégration aisée avec des bibliothèques comme `openai`.

### 6. Streamlit
Bibliothèque Python open-source pour créer des interfaces utilisateur interactives.

- **Caractéristiques principales** :  
  - Création rapide de dashboards et visualisations.  
  - Intégration native avec des bibliothèques comme **Matplotlib**, **Plotly**, et **Altair**.  
  - Support en temps réel pour l'affichage de données et de graphiques.

---

## Conclusion

Ce projet démontre le potentiel des LLM et de l’infrastructure cloud dans des applications professionnelles. Grâce à l’intégration de technologies modernes telles que FastAPI et Scaleway, il ouvre la voie à des solutions innovantes pour la gestion des données et des interactions clients. N'hésitez pas à explorer ce dépôt pour en apprendre davantage et tester par vous-même les capacités offertes !

