from flask import Flask, request
from flask_pymongo import PyMongo
import hashlib
import os
from  dotenv import load_dotenv


load_dotenv()

salt = os.getenv('SALT').encode()

app = Flask(__name__)
app.config['MONGO_URI']= 'mongodb+srv://FacelessDivine:100100101011010110password10010@cluster0.erp3c.mongodb.net/users?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/users', methods = ['POST'])
def create_user():
        # Receiving data
        # print(request.json)
        username = request.json['username']
        password = request.json['password']
        hashed_password = hashlib.pbkdf2_hmac('sha256', password, salt, 100000).hex()
        if username and password:
                id = mongo.db.users.insert(
                        {'username': username, 'password': hashed_password}
                )
                response = {
                        'id': str(id),
                        'username': username,
                        'password': hashed_password
                }
                return response
        else:
                return not_found()
        return {'message': 'Received'}
def not_found(error=None):
        message= {
                'message': 'Resource Not Found',
                'status': 404
        }
        return message
if __name__ == "__main__":
    app.run(debug=True)

















