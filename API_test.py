import requests
import json


def get_weather():
    date = input("Enter the date (yyyy-mm-dd): ")
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    data = json.loads(response.text)
    for item in data['list']:
        if item['dt_txt'].startswith(date):
            print(f"Temperature on {date}: {item['main']['temp']}")


def get_wind_speed():
    date = input("Enter the date (yyyy-mm-dd): ")
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url, verify = False)
    data = json.loads(response.text)
    for item in data['list']:
        if item['dt_txt'].startswith(date):
            print(f"Wind speed on {date}: {item['wind']['speed']}")


def get_pressure():
    date = input("Enter the date (yyyy-mm-dd): ")
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    data = json.loads(response.text)
    for item in data['list']:
        if item['dt_txt'].startswith(date):
            print(f"Pressure on {date}: {item['main']['pressure']}")


while True:
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        get_weather()

    elif choice == 2:
        get_wind_speed()

    elif choice == 3:
        get_pressure()

    elif choice == 0:
        break

print("Program terminated.")