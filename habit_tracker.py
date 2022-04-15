import requests
from _datetime import datetime

PIXEL_END_POINT = "https://pixe.la/v1/users"
USERNAME = "rouge"
GRAPH_ID = "graphone"
TOKEN = "blablablablajsndfdsk"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(PIXEL_END_POINT, json=parameters)
# print(response.text)

GRAPH_END_POINT = f"{PIXEL_END_POINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "CCNA STUDY",
    "unit": "commit",
    "type": "int",
    "color": "ajisai",
}

header = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now()

GRAPH_POST_ENDPOINT = f"{PIXEL_END_POINT}/{USERNAME}/graphs/{GRAPH_ID}"

graph_post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "800",
}

# response = requests.post(url=GRAPH_POST_ENDPOINT, json=graph_post_config, headers=header)
# print(response.text)

GRAPH_UPDATE_ENDPOINT = f"{PIXEL_END_POINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
graph_update_config = {
    "quantity": "1000"
}

GRAPH_DELETE_ENDPOINT = f"{PIXEL_END_POINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=GRAPH_UPDATE_ENDPOINT, headers=header)
print(response.text)
