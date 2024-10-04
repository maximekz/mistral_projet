import os
import requests
from mistralai import Mistral
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Récupérer les clés API
OMDB_API_KEY = os.getenv("OMDB_API_KEY", "6445ade7")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "QQG84DG1tDMvuFN2lkOM9RqlGXOA6w11")

# Initialiser le client Mistral
mistral_client = Mistral(api_key=MISTRAL_API_KEY)

# Fonction pour obtenir les informations d'un film via l'API OMDB
def get_movie_info(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['Response'] == 'True':
            return {
                'Title': data['Title'],
                'Year': data['Year'],
                'IMDb Rating': data['imdbRating'],
                'Plot': data['Plot'],
                'Actors': data['Actors'],
                'Genre': data['Genre']
            }
        else:
            return f"Erreur : {data['Error']}"
    elif response.status_code == 401:
        return "Erreur : Clé API non autorisée. Vérifiez votre clé OMDB."
    else:
        return f"Erreur HTTP: {response.status_code}"

# Fonction pour obtenir un résumé via Mistral
def get_mistral_summary(plot):
    prompt = f"Voici l'intrigue d'un film : {plot}. Peux-tu me faire un résumé de ce film ?"
    response = mistral_client.chat.complete(
        model="mistral-large-latest",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    if response.choices:
        return response.choices[0].message.content
    else:
        return "Aucune réponse obtenue du modèle."

# Fonction pour obtenir des recommandations de films similaires via Mistral
def get_mistral_recommendation(movie_title):
    prompt = f"Je viens de regarder le film '{movie_title}'. Peux-tu me recommander 4 films similaires à celui-ci ?"
    response = mistral_client.chat.complete(
        model="mistral-large-latest",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    if response.choices:
        return response.choices[0].message.content
    else:
        return "Aucune recommandation obtenue du modèle."
