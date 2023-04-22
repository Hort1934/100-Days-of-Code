import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "69f04e4613056b159c2761a9d9e664d2"
account_sid = "AC899afe95efb241928f6c35a4d6bb9557"
auth_token = "95d613570ae53eb2d90e225800c52d7e"

parameters_of_weather = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exlude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=parameters_of_weather)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["hourly"][0]["weather"][0]["id"])
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It`s going to rain today. Remember to bring an umbrella",
        from_='+16813396341',
        to='+380 63 410 9546'
    )
    print(message.status)