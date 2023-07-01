import sensor as data
from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

class tempretureHumidity(Resource):
    def get(self):
        return json.load(data.getInfo())

api.add_resource(tempretureHumidity, "/info")

if (__name__ == "__main__"):
    app.run(host='192.168.178.48', debug=False)