import random

conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Foggy", "Snowy", "Windy", "Partly cloudy"]
cities = ["Piville", "Codeburg", "Pythonia", "Raspberry Bay", "Circuit City", "Binarytown"]
wind_dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
advice = {
    "Sunny": "Great day for a picnic!",
    "Cloudy": "Might want a light jacket.",
    "Rainy": "Bring an umbrella!",
    "Stormy": "Stay indoors if you can!",
    "Foggy": "Drive carefully — low visibility.",
    "Snowy": "Build a snowman!",
    "Windy": "Hold on to your hat!",
    "Partly cloudy": "Pretty nice out there."
}

print("Weather Report Generator")
print("========================")
while True:
    city = random.choice(cities)
    cond = random.choice(conditions)
    temp = random.randint(-5, 35)
    wind = random.randint(0, 60)
    wind_d = random.choice(wind_dirs)
    humidity = random.randint(20, 100)
    print(f"""
--- {city} Weather Report ---
Condition:  {cond}
Temp:       {temp}°C ({temp*9//5+32}°F)
Wind:       {wind} km/h {wind_d}
Humidity:   {humidity}%
Advice:     {advice[cond]}
""")
    if input("New report? (yes/no): ").lower() != "yes":
        break
