# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    pressure = db.Column(db.Float)
    
@app.route('/', methods=['GET'])
def home():
    return "Hello, this is the home page!"

@app.route('/api/sensor_data', methods=['GET'])
def get_sensor_data():
    data = SensorData.query.all()
    sensor_data = [{'temperature': item.temperature, 'humidity': item.humidity, 'pressure': item.pressure} for item in data]
    return jsonify(sensor_data)

@app.route('/api/store_data', methods=['POST'])
def store_data():
    data = request.get_json()
    new_data = SensorData(temperature=data['temperature'], humidity=data['humidity'], pressure=data['pressure'])
    db.session.add(new_data)
    db.session.commit()
    return jsonify(message='Data stockées mon rhoya')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8000)

