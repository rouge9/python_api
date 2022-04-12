import requests
import datetime as dt
import smtplib

MY_LATITUDE = 8.980603
My_LONGTIUDE = 38.757759

def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    # check if iss is passing:
    if MY_LATITUDE+5 <= latitude <= MY_LATITUDE-5 and My_LONGTIUDE+5 <= longitude <= My_LONGTIUDE-5:
        return True


def is_night():

    parameters = {
        "lat": 8.980603,
        "lng": 38.757759,
        "formatted": 0
    }

    response_for_sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response_for_sun.raise_for_status()

    data_for_sun = response_for_sun.json()

    sunrise = int(data_for_sun["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_for_sun["results"]["sunset"].split("T")[1].split(":")[0])
    time = dt.datetime.now().hour
    # check if it is night:
    if sunrise <= time <= sunset:
        return True


# check if iss is overhead and it is night
if is_iss_overhead() and is_night():
    # send email
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("robelgedamu92@gmail.com", "rouge12roba")
    server.sendmail("robelgedamu92@gmail.com", "robelgedamu@gmail.com", "Subject:look up\n\nThe ISS is overhead!")

