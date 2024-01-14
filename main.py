import requests
from datetime import datetime

MY_LAT = 9.320982
MY_LONG = 76.547022

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

iss_tuple = (iss_latitude, iss_longitude)
myloc_tuple = (MY_LAT, MY_LONG)


def iss_near():
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG <= iss_longitude <= MY_LONG:
        print("near me")


# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0,
#     "tzid" : "Asia/Kolkata"
# }
#
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
# sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# time_now = datetime.now()
#
# print(time_now)

#If the ISS is close to my current position
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



