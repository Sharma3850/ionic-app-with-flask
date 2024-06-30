from flask import Flask, jsonify
from flask_cors import CORS 
from random import randint

app = Flask(__name__)
CORS(app, resources={r"/updates": {"origins": "http://localhost:8100"}})
# CORS(app) 


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/updates', methods=['GET'])
def updates():
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

if __name__ == '__main__':
    app.run(debug=True)
