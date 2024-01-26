# -*- coding: utf-8 -*-

# Déclaration des librairies
from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

# Initialise la base de donnée
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)


# Creation de la table Meteo avec les données température humidite et pression chacun comme nombre decimal , une donnée date au format année-mois-jour et un id
class Meteo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    pressure = db.Column(db.Float)
    date = db.Column(db.String(100))


# Endpoint par defaut qui sert de page d'acceuil qui n'est accessible qu'avec une méthode get (ce que l'on fait en utilisant le navigateur)
@app.route('/', methods=['GET'])
def home():
    # Renvoie à l'utilistaeur le fichier index.html qui correspond à la page d'accueil
    return render_template('index.html')


# Endpoint /meteo/ qui renvoie toutes les données stockées dans userInterface.html pour les mettres en formes dans un tableau
@app.route('/meteo/', methods=['GET'])
def user_interface():

    # Récupère toutes les données de la base et les met dans l'ordre décroissant par id donc du plus récent au plus vieux
    data = Meteo.query.order_by(Meteo.id.desc()).all()
    # Créer une liste de json avec toutes les données
    meteo = [{'id' : item.id, 'temperature': item.temperature, 'humidity': item.humidity, 'pressure': item.pressure, 'date': item.date} for item in data]
    # Renvoie la page userInterface.html avec les données
    return render_template('userInterface.html', data=meteo)

# Endpoint /meteo/id qui récupère un seul groupe de donnée en fonction de l'id
@app.route('/meteo/<int:id>', methods=['GET'])
def user_interface_by_id(id):
    # Récupère uniquement les les données qui correspondent à cet id
    data = Meteo.query.get(id)
    # Met les données au format json
    meteo = [{'id' : data.id, 'temperature': data.temperature, 'humidity': data.humidity, 'pressure': data.pressure, 'date': data.date}]
    # Renvoie à l'utilisateur le fichier id.html qui met en forme la donnée
    return render_template('id.html', data=meteo)

# Endpoint meteo pour les données du cubes
@app.route('/api/v1/meteo/', methods=['GET', 'POST'])
# Creation de la fonction
def meteo():
	
	# Premiere methode GET : ce que que demande notre navigateur (il demande au serveur de lui envoyer les données suivantes).
    if request.method == 'GET':
		
		# Data récupère toutes les données dans la table Meteo et les trie par id decroissant (le plus grand en premier donc le dernier ajoute)
        data = Meteo.query.order_by(Meteo.id.desc()).all()
        # Meteo va passer dans chaque valeurs recuperees et mettre sous format json temperatue, humidite et pression
        meteo = [{'id' : item.id, 'temperature': item.temperature, 'humidity': item.humidity, 'pressure': item.pressure, 'date': item.date} for item in data]
        
        return jsonify(meteo)

	# Seconde methode POST : Elle nous permet d'envoyer des donnees au serveur afin qu'il les ajoute a notre table
    elif request.method == 'POST':
        # Data recupere les donnees envoyees par notre requete
        data = request.get_json()
        # New_data associe la cle de chaque valeur recue a une cle de notre table
        new_data = Meteo(temperature=data['temperature'], humidity=data['humidity'], pressure=data['pressure'], date=data['date'])
        # Ajoute les donnees dans la table
        db.session.add(new_data)
        # Sauvegarde notre ajout (.rollback() annulerait l'ajout)
        db.session.commit()
        # Renvoie un message pour confirmer l'ajout des donnees
        return jsonify(message="Data stored successfuly")
	
	# Si la methode utilisee dans la requête est differente alors un message sera renvoyé
    else:
        return jsonify(message='Method unauthorized ! Use GET or POST instead !')

# Endpoint api/v1/meteo/id qui est réservée à la suppression des données
@app.route('/api/v1/meteo/<int:id>', methods=['DELETE'])
def by_id(id):
    # Récupère les données correspondantes à l'id
    data = Meteo.query.get(id)

    # Si la method est bien DELETE
    if request.method == 'DELETE':
        # Et que data à des valeurs
        if data:
            # Suppression des données dans la base
            db.session.delete(data)
            # Le commit permet de sauvegarder la suppression
            db.session.commit()
            # Renvoie un message pour dire que la donnée est bien supprimée
            return jsonify(message=f'Data with ID {id} deleted successfully')
        else:
            return jsonify(message=f'Data with ID {id} not found'), 404
        


# Le swagger est la page qui explique les endpoints et ce à quoi ils servent
SWAGGER_URL = '/swagger' # défini l'endpoin du swagger
API_URL = '/static/swagger.json'  # Assurez-vous de servir votre fichier Swagger JSON statique depuis cette URL

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Swagger Meteo Store"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)



# Ici lorsque nous faisons un python api.py pour la première fois nous créons la base de données et lançons l'api 0.0.0.0 veux dire sur toutes les adresses de l'appareil et port 8000 correspond au port pour accèder à l'api
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8000)

