from flask import Flask, jsonify, render_template_string
import random

app = Flask(__name__)

# HTML Template (inline)
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Weather Monitor App</title>
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(to right, #6dd5fa, #2980b9);
            color: white;
            text-align: center;
            height: 100vh;
            margin: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 0.5em;
        }
        .weather-card {
            background: rgba(255, 255, 255, 0.2);
            padding: 30px 60px;
            border-radius: 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            backdrop-filter: blur(10px);
        }
        .temperature {
            font-size: 3em;
            margin: 10px 0;
            font-weight: bold;
        }
        .condition {
            font-size: 1.5em;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        footer {
            position: absolute;
            bottom: 20px;
            font-size: 0.9em;
            opacity: 0.8;
        }
        button {
            background-color: #ffffff22;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            cursor: pointer;
            font-size: 1em;
            margin-top: 20px;
            transition: background 0.3s ease;
        }
        button:hover {
            background-color: #ffffff44;
        }
    </style>
</head>
<body>
    <h1>🌤 Weather Monitor App</h1>
    <div class="weather-card">
        <div id="temp" class="temperature">-- °C</div>
        <div id="cond" class="condition">Loading...</div>
        <button onclick="getWeather()">🔄 Refresh</button>
    </div>

    <script>
        async function getWeather() {
            const response = await fetch('/weather');
            const data = await response.json();
            document.getElementById('temp').textContent = data.temperature;
            document.getElementById('cond').textContent = data.condition;
        }

        // Auto-update every 5 seconds
        setInterval(getWeather, 5000);
        getWeather();
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

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
