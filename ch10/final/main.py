
from weather import WeatherAPI
from quotes import AdviceAPI

def main():
    advice_api = AdviceAPI()
    forecast_api = WeatherAPI(api_key='cae082c08a5043cf7f980bc86c7e956f')
    advice = advice_api.get_advice()
    city = input("Enter a city: ")
    forecast = forecast_api.get_forecast(lat=37.09, lon=95.71)
    print(f"Here is the forecast for your city: {forecast}\nThis is your advice based on the weather: {advice}")
main()



    


