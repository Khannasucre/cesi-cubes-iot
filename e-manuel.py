import json
import requests

def main():
    url = "http://10.244.128.66:8000/api/v1/meteo/"

    print("Liste des actions : ")
    print("1. Ajouter")
    print("2. Montrer les données stockées")
    print("3. Supprimer")
    print("???????????????????????????")
    choix = int(input("Quelle action veux tu effectuer ?\n"))

    

    match choix :
        case 1 :
            temperature = float(input("Quelle température fait-il ? "))
            humidity =  float(input("Quel est le taux d'humidité ? "))
            pressure =  float(input("Quelle est la pression atmosphérique actuelle ? "))
            data = {
                'temperature' : temperature,
                'humidity' : humidity,
                'pressure' : pressure,
                }

            if data.values():
                post = requests.post(url, json=data)
                print(post.content)
            else:
                print('no data')

        case 2 :
            get = requests.get(url)
            print(get.json())

        case 3 :
            dead_id = input("Numéro du groupe à supprimer : ")
            data = {'id' : dead_id}
            
            if data.values():
                delete = requests.delete(url+dead_id, )

        case 1984 :
            get = requests.get(url)
            get = get.json()
            id = [i['id'] for i in get]
            for i in id : 
                delete = requests.delete(url+ str(i) )
                print(delete)

if __name__ == "__main__":
    main()