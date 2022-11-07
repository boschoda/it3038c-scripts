import json
import requests

r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=45244,us&appid=159c0a9f788563611e4bd8abb5794def')
data = r.json()
print(data['weather'][0]['description'])