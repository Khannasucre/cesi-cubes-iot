# cesi-cubes-iot

# CUBES IOT CESI DI 2023/2024

### Requis
- **Python** et **Internet**
- **Arduino** et **Rasperry Pi**

## DOCUMENTATION : 

### Arduino

**Matériel :**
- Elegoo uno R3
- Sonde BME280 (WPSE335)

**Librairies :**
- https://www.arduino.cc/reference/en/libraries/bme280/
- wire.h (présente par défaut sur Arduino)

**Pour l'utilisation de l'Arduino vous devez suivre les étapes suivantes :**

1. Télécharger la librairie et l'ajouter en librairie sur **Arduino IDE**.
2. Dans **Arduino IDE** importez le code dans le fichier _arduino_code.ino_ présent dans le dossier _arduino_code_.
3. Puis faites un upload sur votre Arduino (par défaut la collecte se fait toutes les 60secondes et les données sont au format 
"température(**en °C**)/humidité(**en %**)/pression(**en Pa**)").
4. A partir de là le script tourne tout seul en boucle.



### Raspberry

Les étapes suivantes sont  à faire après la configuration de base de votre Raspberry :

1. Clonez le répertoire
2. (**OPTIONNEL**) Vous pouvez créer un environnement virtuel sur votre Raspberry pour cloisonner vos librairies vous pouvez le faire en faisant : _$ python -m venv nomdevotreenvironnement_ puis en faisant _$ source nomdevotreenvironnement/bin/activate_.
3. Ensuite vous pouvez téléchargez les dépendances en allant dans le dossier principal du répertoire (**cesi-cube-iot**) puis en faisant _$ pip install -r requirements.txt_.
4. Une fois toutes les dépendances installées, récupérez l'IP de votre appareil en faisant _$ ifconfig_ et remplacez l'IP déjà présente dans _e-manuel.py serialreader.py index.html_ et _swagger.json_ avec votre IP.
5. Branchez votre Arduino sur votre Rasperry en USB et dans votre console tapez _$ ls /dev/tty*_, vous devriez avoir un nom similaire à "/dev/ttyACM0". Copiez le et remplacez le COM3 dans _serialreader.py_ par votre le nom correspondant.
6. Lorsque tout est prêt allez dans _flask/_ (https://github.com/Khannasucre/cesi-cubes-iot/tree/main/flask) et dans votre console faite _$ python api.py_. Cela lancera votre api sur le port 8000 de votre Raspberry.
7. Dans une 2e console, vous devrez faire _$ python serialreader.py_ pour lancer la lecture des données.


## FONCTIONNEMENT

Ce répertoire fonctionne en plusieurs point :
- L'Arduino qui récupère les données et les écrit dans son Serial.
- Le script _serialreader_ qui nous permet de lire ces données et de les envoyer sur l'API.
- Flask qui, une fois lancé, héberge l'api et stocke les données.
