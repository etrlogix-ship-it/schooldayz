try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

def get_weather_fake(city):
    import random
    conditions = ["Sunny", "Cloudy", "Rainy", "Partly Cloudy"]
    temp = random.randint(-5, 35)
    return {"city": city, "temp": temp, "condition": random.choice(conditions),
            "humidity": random.randint(30, 90), "wind": random.randint(0, 60)}

print("Live Weather Checker")
print("====================")

if not HAS_REQUESTS:
    print("Note: requests not installed. Using simulated data.")
    print("Install with: pip3 install requests --break-system-packages")

while True:
    city = input("\nEnter city name (or quit): ").strip()
    if city.lower() == "quit": break
    
    if HAS_REQUESTS:
        # Using Open-Meteo (free, no API key needed)
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        try:
            geo = requests.get(geo_url, timeout=5).json()
            if not geo.get("results"):
                print(f"City not found: {city}")
                continue
            loc = geo["results"][0]
            lat, lon = loc["latitude"], loc["longitude"]
            name = loc["name"]
            
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=relativehumidity_2m"
            weather = requests.get(weather_url, timeout=5).json()
            cw = weather["current_weather"]
            
            codes = {0:"Clear sky",1:"Mainly clear",2:"Partly cloudy",3:"Overcast",
                     45:"Foggy",51:"Light drizzle",61:"Slight rain",71:"Light snow",
                     80:"Slight showers",95:"Thunderstorm"}
            condition = codes.get(cw["weathercode"], f"Code {cw['weathercode']}")
            
            print(f"\nWeather in {name}:")
            print(f"  Temperature: {cw['temperature']}°C")
            print(f"  Condition: {condition}")
            print(f"  Wind speed: {cw['windspeed']} km/h")
        except Exception as e:
            print(f"Error fetching weather: {e}")
            data = get_weather_fake(city)
            print(f"Using simulated data for {city}: {data['temp']}°C, {data['condition']}")
    else:
        data = get_weather_fake(city)
        print(f"\n(Simulated) Weather in {data['city']}:")
        print(f"  Temperature: {data['temp']}°C")
        print(f"  Condition: {data['condition']}")
        print(f"  Humidity: {data['humidity']}%")
        print(f"  Wind: {data['wind']} km/h")
