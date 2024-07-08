from flask import Flask, jsonify, request
from flask_cors import CORS
from random import randint
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'secret_key'

users = {}

# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(150), nullable=False

@app.route('/')
def hello_world():
    return 'Hello, User! Api is up and running!!!...'

@app.route('/updates', methods=['GET', 'POST'])
def updates():
    if request.method == 'GET':
        data = {
            'Temperature': randint(0, 50),
            'Followers': randint(0, 50),
            'Likes': randint(0, 50),
            'Stars': randint(0, 50),
            'Completed': randint(0, 50),
            'Warnings': randint(0, 50),
            'Notifications': randint(0, 50)
        }
        return jsonify(data)
    
    elif request.method == 'POST':
        print("hitting post")
        if request.is_json:
            data = request.get_json()
            print(data)
            return jsonify({"message": "Data received", "data": data})
        else:
            return jsonify({"message": "Request must be JSON"}),

@app.route('/signup', methods=['POST'])
def signup():
    print("signup hitting")
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({"message": "User already exists"}),

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    users[username] = hashed_password

    # Commented out database logic
    # new_user = User(username=username, password=hashed_password)
    # db.session.add(new_user)
    # db.session.commit()

    return jsonify({"message": "User created successfully"}),

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user_password = users.get(username)
    if not user_password or not check_password_hash(user_password, password):
        return jsonify({"message": "Invalid username or password"}),

    token = jwt.encode({
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }, app.config['SECRET_KEY'])

    return jsonify({"token": token})

if __name__ == '__main__':
    app.run(debug=True)
