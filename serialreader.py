# Déclaration des librairies
from datetime import datetime
import requests
import serial
import time

# Url ou envoyer les données si l'api tourne sur le même appareil vous n'avez pas besoin de le changer sinon remplacez localhost par l'ip de votre appareil
url = 'http://localhost:8000/api/v1/meteo/'

# Nom du port ou l'arduino est branché
port = '/dev/ttyACM0' 

# Baud rate correspond à la fréquence de transmission des données ici et dans le script Arduino 115200
baud_rate = 115200

# serial.Serial est une fonction de la librairie serial qui lis les données écrites dans le serial Arduino
ser = serial.Serial(port, baud_rate)

while True:

    # Création d'une donnée date en passant par un timestamp
    timestamp = int(time.time()) + 3600
    date =  datetime.utcfromtimestamp(timestamp)
    date = date.strftime('%Y-%m-%d %H:%M:%S')

    # Lecture de la dernière ligne écrite dans le serial
    line = ser.readline().decode('utf-8').strip()
    print(line)

    # Si la ligne commence par "Found" qui à l'initialisation détecte si la sonde est présente renvoie "Found BME280 sensor! Success." alors écrit "Not now"
    if line[:5] == "Found":
        print("Not now")
    
    # Sinon le script va commencer à traiter les données
    else :
        # Ici les données sont écrites au format xxx/xxx/xxx
        # Les données sont séparées dans une liste [xxx,xxx,xxx] grâce aux "/"
        a = line.split("/")
        print(a)
        # Data est au format Json càd une Key et une valeur pour intéragir avec l'api
        # On met à chaque key sa valeur correspondante dans la liste et la date
        data = {
            "temperature" : float(a[0]),
            "humidity" : float(a[1]),
            "pressure" : float(a[2]),
            "date" : date
        }
        print(data)
        # Si data à des valeurs alors une requête post est envoyée à l'api qui sera traitée par api.py et nous écrivons la réponse de la requête
        if data.values():
            post = requests.post(url,json=data)
            print(post.content)
        # sinon nous écrivons juste 'no data'
        else:
            print('no data')
