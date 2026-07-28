import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_log.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

plt.figure(figsize=(12, 6))

for city in df["city"].unique():
    city_data = df[df["city"] == city]
    plt.plot(city_data["timestamp"], city_data["temperature_c"], marker="o", label=city)

plt.title("Temperature Over Time by Locality (Trivandrum)")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temperature_chart.png")

print("Chart saved as temperature_chart.png")