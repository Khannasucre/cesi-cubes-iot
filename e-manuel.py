import json
import requests

def main():
    url_flask = "http://localhost:8000/api/meteo/"
    url_django = "http://localhost:8000/meteo"

    print("Quel Api veux tu utiliser ?")
    print("1. Flask")
    print("2. Django")

    choix_api = int(input("Entre le numéro correspondant\n"))

    match choix_api:
        case 1:
            url = url_flask
        case 2:
            url = url_django


    print("Liste des actions : ")
    print("1. Ajouter")
    print("2. Montrer les données stockées")
    # print("2. Modifier")
    # print("3. Supprimer")
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


        # case 2 :
        #     old_name = input("Ancien nom de ton groupe: ")
        #     old_id = input("ID nom de ton groupe: ")
        #     new_name = input("Nouveau nom de ton groupe: ")
        #     payload = {'name' : new_name, }#'id' : old_id}
        #     if payload.values():
        #         put = requests.put(url+old_id, data=payload)
        #         print(put.content)



        # case 3 :
        #     dead_id = input("Numéro du groupe à supprimer : ")
        #     data = {'id' : dead_id}
            
        #     if data.values():
        #         deletr = requests.delete(url+dead_id, )



if __name__ == "__main__":
    main()