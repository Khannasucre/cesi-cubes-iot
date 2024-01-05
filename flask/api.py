# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request,  render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

#Creation de la table Meteo avec les données température humidite et pression chacun comme nombre decimal et un id qui s
class Meteo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    pressure = db.Column(db.Float)

#Endpoint par defaut qui sert de page d'acceuil
@app.route('/', methods=['GET'])
def home():
    return "<h1>Coucou, si tu arrives içi tu es au bon endroit jeune DI</h1><h3>Nous te reverrons Juju!</h3><h6>Et toi loic c'est pas grave si on ne te vois plus</h6>"

#Endpoint meteo pour les données du cubes
@app.route('/api/v1/meteo/', methods=['GET', 'POST'])
#creation de la fonction
def meteo():
	
	#Premiere methode GET : ce que que demande notre navigateur (il demande au serveur de lui envoyer les données suivantes).
    if request.method == 'GET':
		
		#data récupère toutes les données dans la table Meteo et les trie par id decroissant (le plus grand en premier donc le dernier ajoute)
        data = Meteo.query.order_by(Meteo.id.desc()).all()
        #meteo va passer dans chaque valeurs recuperees et mettre sous format json temperatue, humidite et pression
        meteo = [{'temperature': item.temperature, 'humidity': item.humidity, 'pressure': item.pressure} for item in data]
        return jsonify(meteo)
	
	#Seconde methode POST : Elle nous permet d'envoyer des donnees au serveur afin qu'il les ajoute a notre table
    elif request.method == 'POST':
        #data recupere les donnees envoyees par notre requete
        data = request.get_json()
        #new_data associe la cle de chaque valeur recue a une cle de notre table
        new_data = Meteo(temperature=data['temperature'], humidity=data['humidity'], pressure=data['pressure'])
        #ajoute les donnees dans la table
        db.session.add(new_data)
        #sauvegarde notre ajout (.rollback() annulerait l'ajout)
        db.session.commit()
        #renvoie un message pour confirmer l'ajout des donnees
        return jsonify(message="Data stored successfuly")
	
	#Si la methode utilisee dans la requête est differente alors un message sera renvoyé
    else:
        return jsonify(message='Method unauthorized ! Use GET or POST instead !')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8000)

