from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Weather Monitor App is running!"})

@app.route('/weather')
def get_weather():
    temp = round(random.uniform(15.0, 35.0), 2)
    condition = random.choice(["Sunny", "Rainy", "Cloudy", "Windy"])
    return jsonify({
        "temperature": f"{temp} °C",
        "condition": condition
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
