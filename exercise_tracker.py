import os

import requests
from datetime import datetime


APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
SHETTY_AUT_TOKEN = os.environ.get("SHETTY_AUT")
URL_FOR_SHETTY_END_POINT = os.environ.get("SHETTY_URL")

header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0",
}

header_sheets = {
    "Authorization": SHETTY_AUT_TOKEN
}


parameters = {
    "query": input("Tell me which exercise you did: "),

}

response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", headers=header, json=parameters)
print(response.text)

data = response.json()
for n in data["exercises"]:
    exercise_data = n["name"].title()
    duration_data = n["duration_min"]
    calories_data = n["nf_calories"]

    date = datetime.now().date().strftime("%Y/%m/%d")
    time = datetime.now().time().strftime("%I:%M:%S")

    parameters_for_post = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_data,
            "duration": duration_data,
            "calories": calories_data
        }
    }


    response_post = requests.post(url=URL_FOR_SHETTY_END_POINT, json=parameters_for_post, headers=header_sheets)
    print(response_post.text)
