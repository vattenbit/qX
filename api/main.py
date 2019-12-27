#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)

from pymongo import MongoClient
import utils
import os

print("Initialing...")

# Load Flask variables
flask_port = os.getenv('FLASK_PORT')
flask_host = os.getenv('FLASK_HOST')

# Connection to MongoDB
connection_url = os.getenv('MONGO_CONNECTION')
client = MongoClient(connection_url)

# Init Flask and Parser for POST calls
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

# Class of API
class User(Resource):
    def get(self, nick):
        return utils.bson_to_json(client.qx_db.users.find_one({"nick":nick}))

class Token(Resource):
    def post(self):
        # input Args
        parser.add_argument('pass_md5', type=str)
        parser.add_argument('nick', type=str)
        args = parser.parse_args()
        #Get user with nick and password
        user = utils.bson_to_json(client.qx_db.users.find_one({"nick":args.get('nick'), "password":args.get('pass_md5')}))
        return {"token":"your_token"}

# Add Resources to API
api.add_resource(User, '/user/<nick>')
api.add_resource(Token, '/token')

# Run Flask
if __name__ == '__main__':
    app.run(debug=True, port=flask_port, host=flask_host)
