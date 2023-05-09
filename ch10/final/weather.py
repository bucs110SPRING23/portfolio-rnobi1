import requests

class WeatherAPI:
    def __init__(self, api_key ):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_forecast(self, lat, lon):
        url = f"{self.base_url}?lat={lat}&lon={lon}&appid={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_data = {
                "description": description,
                "temperature": temperature,
                "humidity": humidity
            }
            return weather_data
        else: 
            return f"Failed to get weather forecast for your city. Error code: {response.status_code}"


