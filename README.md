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

