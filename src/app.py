from flask import Flask, request, Response
from flask_pymongo import pymongo
import hashlib
import os
from  dotenv import load_dotenv
from flask.json import jsonify
from bson import json_util
from bson.objectid import ObjectId
import dbconfig as db
load_dotenv()

salt = os.getenv('SALT').encode()
# print(salt) 
app = Flask(__name__)



@app.route('/users/<id>', methods=['GET'])
def get_user(id):
        user = db.c_users.users.find_one({'_id': ObjectId(id)})
        response = json_util.dumps(user)
        return Response(response, mimetype= 'application/json')

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
        db.c_users.users.delete_one({'_id': ObjectId(id)})
        response = jsonify({'message': 'User: '+ id + ' was deleted successfully'})
        return response
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
        username = request.json['username']
        password = request.json['password'].encode()
        if username and password:
                hashed_password = hashlib.pbkdf2_hmac('sha512', password, salt, 100000).hex()
                db.c_users.users.update_one({'_id': ObjectId(id)}, {'$set':{
                'username': username,
                'password': hashed_password
                }})
                response =  jsonify({'message': 'User: '+ id + ' was updated successfully'})
                return response

@app.route('/users', methods=['GET'])
def get_users():
        users = db.c_users.users.find()
        response = json_util.dumps(users)
        return Response(response, mimetype='application/json')

@app.route('/users', methods = ['POST'])
def create_user():
        # Receiving data
        # print(request.json)
        username = request.json['username']
        password = request.json['password'].encode()
        

        if username and password:
                hashed_password = hashlib.pbkdf2_hmac('sha512', password, salt, 100000).hex()
                db.c_users.users.insert(
                        {'username': username, 'password': hashed_password}
                )
                response = {
                        'id': 1,
                        'username': username,
                        'password': hashed_password
                }
                # return {'message': 'Received'}
                return response
        else:
                return not_found()
        return {'message': 'Received'}
@app.errorhandler(404)
def not_found(error=None):
        response = jsonify({
                'message': 'Resource Not Found',
                'status': 404
        })
        response.status_code = 404
        return response
if __name__ == "__main__":
    app.run(debug=True)

















