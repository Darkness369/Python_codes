from flask import Flask, request
from flask_pymongo import PyMongo
import hashlib
import os
from  dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI']= 'mongodb://localhost/apiusers'

mongo = PyMongo(app)

@app.route('/users', methods = ['POST'])
def create_user():
        # Receiving data
        # print(request.json)
        username = request.json['username']
        password = request.json['password']
        if username and password:
                mongo.db.users.insert(
                        {'username': username, 'password': password}
                )
                return {"message": "Usuario guardado"}
        else:
                return {'message': 'error'}

if __name__ == "__main__":
    app.run(debug=True)

