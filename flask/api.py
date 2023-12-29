# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request,  render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class Meteo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    pressure = db.Column(db.Float)
    
@app.route('/', methods=['GET'])
def home():
    return "<h1>Coucou, si tu arrives içi tu es au bon endroit jeune DI</h1><h3>Nous te reverrons Juju!</h3><h6>Et toi loic c'est pas grave si on ne te vois plus</h6>"

@app.route('/api/meteo/', methods=['GET', 'POST'])

def meteo():

    if request.method == 'GET':

        data = Meteo.query.order_by(Meteo.id.desc()).all()
        meteo = [{'temperature': item.temperature, 'humidity': item.humidity, 'pressure': item.pressure} for item in data]
        return render_template('meteo.html', meteo=meteo)
        #return jsonify(meteo)

    elif request.method == 'POST':
        
        data = request.get_json()
        new_data = Meteo(temperature=data['temperature'], humidity=data['humidity'], pressure=data['pressure'])
        db.session.add(new_data)
        db.session.commit()
        return jsonify(message='Data dans le baba mon Khoya')

    else:
        return jsonify(message='Pas la bonne method mon crampté au sucres :( !')

# @app.route('/api/store_data/', methods=['POST'])
# def store_data():
#     data = request.get_json()
#     new_data = Meteo(temperature=data['temperature'], humidity=data['humidity'], pressure=data['pressure'])
#     db.session.add(new_data)
#     db.session.commit()
#     return jsonify(message='Data stockées mon Khoya')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8000)

