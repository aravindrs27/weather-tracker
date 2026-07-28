import os
import csv
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

latitude = 8.5241
longitude = 76.9366

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url, params=params)
data = response.json()

# Pull out just the fields we care about
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]
city = data["name"]
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"{timestamp} | {city} | {temperature}°C (feels like {feels_like}°C) | {humidity}% humidity | {description}")

# File where we'll keep appending each reading
csv_file = "weather_log.csv"
file_exists = os.path.isfile(csv_file)

with open(csv_file, mode="a", newline="") as f:
    writer = csv.writer(f)
    # Write header only if the file is brand new
    if not file_exists:
        writer.writerow(["timestamp", "city", "temperature_c", "feels_like_c", "humidity_pct", "description"])
    writer.writerow([timestamp, city, temperature, feels_like, humidity, description])

print(f"Saved to {csv_file}")