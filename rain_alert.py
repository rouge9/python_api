import requests
import os

API_KEY = f"{os.environ['OWM_API']}"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": 7.012170,
    "lon": 39.973480,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:24]
is_raining = False
for hour_data in weather_slice:
    rain_data = hour_data["weather"][0]["id"]
    if int(rain_data) < 700:
        is_raining = True

if is_raining:
    url = "https://sms77io.p.rapidapi.com/sms"
    payload = f"to=%2B251941184014&p={os.environ['sms']}&text=bring%20an%20umbrella"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Host": "sms77io.p.rapidapi.com",
        "X-RapidAPI-Key": f"{os.environ['sms']}",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.status_code)
