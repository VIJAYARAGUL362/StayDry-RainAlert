# IMPORTING LIBRARIES
import requests
import smtplib
from dotenv import load_dotenv
import os

# LOADING ENVIRONMENT VARIABLE
load_dotenv(dotenv_path="rain_alert.env")



# GLOBAL VARIABLES
MY_LONG = "80.270721"
MY_LAT = "13.082680"
API_KEY = "d7d83d00164325e417af3332d34e5278"
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
MY_EMAIL = "vijayaragul2005@gmail.com" # your email
TO_EMAIL = "wearevr2005@gmail.com"
PASSWORD = os.getenv("MY_EMAIL_PASS")


parameters = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":API_KEY,
    "cnt":4,

}


response = requests.get(url=API_ENDPOINT,params=parameters)
response.raise_for_status()

weather_data = response.json()

for i in range(len(weather_data["list"])):
    if (weather_data["list"][i]["weather"][0]["id"]) > 700:
        rain = False
    else:
        rain = True
        break

if rain:
  with smtplib.SMTP("smtp.gmail.com") as connections:
      connections.starttls()
      connections.login(user=MY_EMAIL,password=PASSWORD)
      connections.sendmail(from_addr=MY_EMAIL,to_addrs=TO_EMAIL,msg="Subject:Rain alert\n\n Hey it is going to be raining in your area so take a umbrella ")

