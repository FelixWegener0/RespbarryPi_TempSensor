import sensor as data
from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

class temperature(Resource):
    def get(self):
        return jsonify(data.getTemperature())

class humidity(Resource):
    def get(self):
        return jsonify(data.getHumidity())

class testConnection(Resource):
    def get(self):
        return jsonify('test_Connection')

api.add_resource(temperature, "/temp")
api.add_resource(humidity, "/humidity")
api.add_resource(testConnection, "/testConnect")

if (__name__ == "__main__"):
    app.run(host='192.168.178.48', debug=True)