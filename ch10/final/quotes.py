import requests

class AdviceAPI:
    def __init__(self):
        self.url = 'https://api.adviceslip.com/advice'

    def get_advice(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            advice_data = response.json()['slip']
            advice = advice_data['advice']
            return advice
        else:
            return None 
