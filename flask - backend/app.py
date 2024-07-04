from flask import Flask, jsonify, request
from flask_cors import CORS
from random import randint

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

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
            return jsonify({"message": "Request must be JSON"}), 400
        

@app.route('/submit', methods=['POST'])
def submit_data():
    print("hitting submit")
    if request.is_json:
        data = request.get_json()
        print(data)
        return jsonify({"message": "Data received", "data": data})
    else:
        return jsonify({"message": "Request must be JSON"}), 400
        
if __name__ == '__main__':
    app.run(debug=True)
