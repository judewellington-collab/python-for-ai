import requests

def get_weather(latitude, longitude):
    # Build the API URL with our parameters
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

    # Make the request
    response = requests.get(url)
    data = response.json()

    return data["current"]["temperature_2m"]

# We need coordinates to get weather data
thoothukudi_weather=get_weather(8.764166, 78.134834)
print(f"current temperature in thoothukudi is {thoothukudi_weather}°C")

chennai_weather=get_weather(13.0827, 80.2707)
print(f"current temperature in chennai is {chennai_weather}°C")

bangalore_weather=get_weather(12.971599, 77.594566)
print(f"current temperature in bangalore is {bangalore_weather}°C")
