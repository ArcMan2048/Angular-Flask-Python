from flask import Flask, jsonify;
from flask_cors import CORS;

app = Flask(__name__)
CORS(app)



weather = {
     "data": [
     {
         "day": "1/6/2019",
         "temperature": "23",
         "windspeed": "16",
         "event": "Sunny"
     },
     {
         "day": "2/6/2019",
         "temperature": "25",
         "windspeed": "14",
         "event": "Hot"
     },
     {
         "day": "3/6/2019",
         "temperature": "29",
         "windspeed": "12",
         "event": "Very Hot"
     },
     {
         "day": "4/6/2019",
         "temperature": "25",
         "windspeed": "20",
         "event": "Windy"
     },


     ]
    }

@app.route("/weatherReport/", methods=['GET'])
def weatherReport():
    global weather
    return jsonify([weather])

if __name__ == '__main__':
    app.run(debug=True)
