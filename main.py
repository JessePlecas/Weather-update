import requests
import os
from twilio.rest import Client

api_key = ["Enter API Key"]
end_point = "https://api.openweathermap.org/data/2.8/onecall"
account_sid = 'AC73c526c26dd71848c8fed570143aa8a9'
auth_token = ["Enter auth token"]

weather_params = {
    "lat": ["Enter your latitude"],
    "lon" : ["Enter your longitude"],
    "exclude": "current,minutely,daily",
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url=end_point, params=weather_params)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:17]

will_rain = False

for hour_data in weather_slice:
    degrees = (hour_data["temp"])
    weather_code = hour_data["weather"][0]["id"]

    if int(weather_code) < 700:
        will_rain = True
        weather_code = f"Rain today "
    else:
        weather_code = "No rain today "

if will_rain:

    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                            body=f'{weather_code}',
                            from_='+12568575645',
                            to='enter a number'
                        )