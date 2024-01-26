# Déclaration des librairies
import json
import requests
import time
from datetime import datetime


def main():
    # Url où faire l'action changer l'ip en fonction de votre appareil
    url = "http://10.244.128.66:8000/api/v1/meteo/"


    # Dans la console propose une liste de choix
    print("Liste des actions : ")
    print("1. Ajouter")
    print("2. Montrer les données stockées")
    print("3. Supprimer")

    # Enregistre la réponse de l'utilisateur
    choix = int(input("Quelle action veux tu effectuer ?\n"))

    
    # Condition en fonction du choix de l'utilisateur
    match choix :
        # Ajouter
        case 1 :
            # Création d'une donnée date en passant par un timestamp
            timestamp = int(time.time()) + 3600
            date =  datetime.utcfromtimestamp(timestamp)
            date = date.strftime('%Y-%m-%d %H:%M:%S')

            # Demande à l'utilisateur les données à mettre
            temperature = float(input("Quelle température fait-il ? "))
            humidity =  float(input("Quel est le taux d'humidité ? "))
            pressure =  float(input("Quelle est la pression atmosphérique actuelle ? "))
            data = {
                'temperature' : temperature,
                'humidity' : humidity,
                'pressure' : pressure,
                'date' : date,
                }

            # Si data à des valeurs alors une requête post est envoyée à l'api qui sera traitée par api.py et nous écrivons la réponse de la requête
            if data.values():
                post = requests.post(url, json=data)
                print(post.content)
            # Sinon écrit 'no data'
            else:
                print('no data')

        # Montrer les données
        case 2 :
            # Requête get qui récupère toute les données stockées
            get = requests.get(url)
            # Les écrit dans la console au format json ({'key' : value})
            print(get.json())

        # Supprimer 1 données
        case 3 :
            # Demande à l'utilisteur l'id à supprimer
            dead_id = input("Id la donnée à supprimer : ")
            
            
            # Envoie une requête delete avec l'id à supprimer 
            delete = requests.delete(url+dead_id, )
        
        # Supprimes toutes les données présentes de l'api
        case 1984 :
            # Récupère toutes les données
            get = requests.get(url)
            get = get.json()
            # Sur la totalité des données récupère à chaque fois l'id
            id = [i['id'] for i in get]
            # Pour chaque id une requête delete est envoyée
            for i in id : 
                delete = requests.delete(url+ str(i) )
                print(delete)

if __name__ == "__main__":
    main()