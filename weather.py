import requests
import json

api = "http://api.openweathermap.org/data/2.5/weather?q=London&APPID=6006c8a1d90dd8e603fc35057667698f"
r = requests.get(api)
data = json.loads(r.text)
print("都市"+ ":" + data["name"])
print("天気"+ ":" + data["weather"][0]["description"])
print("base"+ ":" + data["base"])
