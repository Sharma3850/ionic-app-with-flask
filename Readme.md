# Cross-Platform Weather App
A simple cross-platform weather application built using Ionic Angular for the frontend and Flask for the backend. The application fetches random weather data from the Flask API and displays it on the frontend.


**Features:**
Randomly generated weather data
Cross-origin resource sharing (CORS) enabled
Simple and clean UI with Ionic framework


**Prerequisites:**
Node.js and npm
Python 
Ionic CLI
Flask 
Frontend (Ionic Angular)


**instructions to run the app**
Serve the Ionic application: ionic serve

Backend (Flask)
Navigate to the backend directory
Create a virtual environment
Activate the virtual environment
Install dependencies: pip install -r requirements.txt

Run the Flask server:flask run

Usage
Start the Flask backend server (if not already running):    flask run


Serve the Ionic frontend application (if not already running):  ionic serve


Access the application in your browser at http://localhost:your_port.

API
The Flask backend exposes the following endpoint:

GET /updates

Returns random weather data including temperature, followers, likes, stars, completed tasks, warnings, and notifications.


Project Structure:
plaintext
Copy code
weather-app/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── ...
├── frontend/
│   ├── src/
│   ├── angular.json
│   ├── package.json
│   └── ...
└── README.md