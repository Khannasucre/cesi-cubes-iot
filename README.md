# cesi-cubes-iot

# CUBES IOT CESI DI 2023/2024

## Requis
-> Python et internet
-> Arduino et Rasperry

##DOCUMENTATION

#Arduino
Matériel :
-> Elegoo uno R3
-> sonde bme280 (WPSE335)
Librairie :
-> https://www.arduino.cc/reference/en/libraries/bme280/
-> wire.h (présente par défaut sur arduino)

Pour l'utilisation de l'arduino vous devez suivre les étapes suivantes :

-> Télécharger la librairie et l'ajouter en librairie sur Arduino IDE
-> Dans Arduino IDE importez le code dans le fichier arduino_code.ino présent dans le dossier arduino_code
-> Puis faites un upload sur votre Arduino (par défaut la collecte se fait toutes les 60secondes et les données sont au format 
"température(en°C)/humidité(en%)/pression(enPa))
-> A partir de là le script tourne tout seul en boucle.



#Rasperry

Les étapes suivantes sont  à faire après la configuration de base de votre rasperry :
-> Clonez le répertoire
-> (OPTIONNEL) vous pouvez créer un environement virtuel sur votre rasperry pour cloisonner vos librairies vous pouvez le faire en faisant : $ python -m venv _nomdevotreenvironnement_ puis en faisant _$ source nomdevotreenvironnement/bin/activate_
->Ensuite vous pouvez téléchargez les dépendances en allant dans le dossier principal du répertoire (cesi-cube-iot) puis en faisant _$ pip install -r requirements.txt_
-> Une fois toutes les dépendances installées récupérez l'ip de votre appareil en faisant _$ ifconfig_ et remplacez l'ip déjà présente dans e-manuel.py serialreader.py index.html et swagger.json avec votre ip.
-> Branchez votre arduino sur votre rasperry en usb et dans votre console tapez _$ ls /dev/tty*_ vous devriez avoir un nom similaire à "/dev/ttyACM0" copiez le et remplacez le COM3 dans serialreader.py par votre le nom correspondant.
-> Lorsque tout est prêt allez dans flask/ et dans votre console faite _$ python api.py_ ce qui lancera votre api sur le port 8000 de votre rasperry.


