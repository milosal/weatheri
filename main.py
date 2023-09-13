import requests

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

def display_weather(data):
    if data:
        print(f"------\nWeather in {city}\n------")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Temperature: {round((data['main']['temp'])*(9/5) + 32, 1)}°F")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("No weather data available.")

if __name__ == "__main__":
    try:
        with open("key.txt", "r") as file:
            api_key = file.read().strip()
    except FileNotFoundError:
        print("Could not find the file with your key.")
        api_key = None
    city = input("Enter the name of a city: ")

    weather_data = get_weather(api_key, city)
    display_weather(weather_data)
