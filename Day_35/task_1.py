import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "618705b92bc1e04bb5267cab96095339"

parameters_of_weather = {
    "lat": 50.447731,
    "lon": 30.542721,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=parameters_of_weather)
print(response.json())