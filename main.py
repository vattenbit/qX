#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api
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

# Init Flask
app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self, nick):
        return utils.bson_to_json(client.qx_db.users.find_one({"nick":nick}))

api.add_resource(User, '/user/<nick>')

if __name__ == '__main__':
    app.run(debug=True, port=flask_port, host=flask_host)




#client = MongoClient(connection_url)

#db = client.business
#a = {"a":"a"}
#insert = db.reviews.insert_one(a)
