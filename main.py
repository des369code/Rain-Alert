import requests
import smtplib
import os

MY_LAT = 3.0798396754365855
MY_LONG = 101.62530233046918
MY_EMAIL = "ddesmaandesmaan@gmail.com"
MY_PASSWORD = os.environ.get("MY_PASSWORD")
RECEIVER_EMAIL = "ddesmaandesmaan@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

#API Key
# A personal account number and password
# The way how the API provider can track how much you are using their API

api_key = os.environ.get("api_key")

#API Endpoint Parameters
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

api_endpoint = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
api_endpoint.raise_for_status()

weather_data = api_endpoint.json()
# print(weather_data)

# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False

for i in weather_data["list"]:
    condition_code = int(i["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    subject = "Rain Alert !!!"
    body = "It's going to rain in the next 3 hours. Remember to bring an umbrella!"
    message = f"Subject:{subject}\n\n{body}"

    with smtplib.SMTP(SMTP_SERVER, port=SMTP_PORT) as connection:
        connection.starttls()  # Encrypts the connection
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=RECEIVER_EMAIL, msg=message
        )
    print("Email sent successfully.")
