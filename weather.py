import os
import csv
from datetime import datetime, timezone, timedelta
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

# Localities within Trivandrum district
cities = {
    "Kazhakkoottam": (8.5647, 76.8681),
    "Sreekaryam": (8.5461, 76.9271),
    "Pattom": (8.5148, 76.9530),
    "Vazhuthacaud": (8.5033, 76.9500),
    "Palayam": (8.5010, 76.9530),
    "Kowdiar": (8.5170, 76.9600),
    "Peroorkada": (8.5350, 76.9600),
    "Nedumangad": (8.6030, 77.0000),
    "Neyyattinkara": (8.4009, 77.0850),
    "Kovalam": (8.4004, 76.9787),
}

url = "https://api.openweathermap.org/data/2.5/weather"

IST = timezone(timedelta(hours=5, minutes=30))
timestamp = datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S")

csv_file = "weather_log.csv"
file_exists = os.path.isfile(csv_file)

with open(csv_file, mode="a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["timestamp", "city", "temperature_c", "feels_like_c", "humidity_pct", "description"])

    for city_label, (lat, lon) in cities.items():
        params = {
            "lat": lat,
            "lon": lon,
            "appid": api_key,
            "units": "metric"
        }
        response = requests.get(url, params=params)
        data = response.json()

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print(f"{timestamp} | {city_label} | {temperature}°C (feels like {feels_like}°C) | {humidity}% humidity | {description}")

        writer.writerow([timestamp, city_label, temperature, feels_like, humidity, description])

print(f"Saved to {csv_file}")