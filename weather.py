import requests
import json

api = "http://api.openweathermap.org/data/2.5/weather?q=London&APPID=APIkey"
r = requests.get(api)
data = json.loads(r.text)
print("都市"+ ":" + data["name"])
print("天気"+ ":" + data["weather"][0]["description"])
print("base"+ ":" + data["base"])
