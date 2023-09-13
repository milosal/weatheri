import requests
from flask import Flask, request, jsonify

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data.")
        return None

@app.route('/get_weather', methods=['GET'])
def get_weather_route():
    try:
        with open("key.txt", "r") as file:
            api_key = file.read().strip()
    except FileNotFoundError:
        print("Could not fine file with your key. Please name it 'key.txt'.")
        api_key = None
    city = request.args.get('city')
    weather_data = get_weather(api_key, city)
    return jsonify(weather_data)

if __name__ == "__main__":
    app.run(debug=True)

