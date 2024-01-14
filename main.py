import requests
import smtplib
import time

MY_LAT = xxx
MY_LONG = yyy

my_mail = "krizhnatester@gmail.com"
password = ""

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

iss_tuple = (iss_latitude, iss_longitude)
myloc_tuple = (MY_LAT, MY_LONG)


def iss_near():
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


while True:
    time.sleep(60)
    if iss_near():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(
                from_addr=my_mail,
                to_addrs="",
                msg=f"Subject:ISS Overhead \n\nGO out and Look up, there is the ISS"
            )




