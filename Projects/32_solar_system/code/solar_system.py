planets = {
    "Mercury": {
        "distance_km": 57_900_000,
        "diameter_km": 4_879,
        "moons": 0,
        "day_hours": 1407,
        "year_days": 88,
        "temp_c": 167,
        "fact": "Mercury has no atmosphere and extreme temperature swings!"
    },
    "Venus": {
        "distance_km": 108_200_000,
        "diameter_km": 12_104,
        "moons": 0,
        "day_hours": 5832,
        "year_days": 225,
        "temp_c": 465,
        "fact": "Venus is hotter than Mercury despite being further from the Sun!"
    },
    "Earth": {
        "distance_km": 149_600_000,
        "diameter_km": 12_742,
        "moons": 1,
        "day_hours": 24,
        "year_days": 365,
        "temp_c": 15,
        "fact": "Earth is the only known planet with liquid water on its surface."
    },
    "Mars": {
        "distance_km": 227_900_000,
        "diameter_km": 6_779,
        "moons": 2,
        "day_hours": 25,
        "year_days": 687,
        "temp_c": -65,
        "fact": "Mars has the tallest volcano in the solar system — Olympus Mons!"
    },
    "Jupiter": {
        "distance_km": 778_600_000,
        "diameter_km": 139_820,
        "moons": 95,
        "day_hours": 10,
        "year_days": 4333,
        "temp_c": -110,
        "fact": "Jupiter's Great Red Spot is a storm that has lasted 350+ years!"
    },
    "Saturn": {
        "distance_km": 1_433_500_000,
        "diameter_km": 116_460,
        "moons": 146,
        "day_hours": 11,
        "year_days": 10759,
        "temp_c": -140,
        "fact": "Saturn could float on water — it is less dense than water!"
    },
    "Uranus": {
        "distance_km": 2_872_500_000,
        "diameter_km": 50_724,
        "moons": 28,
        "day_hours": 17,
        "year_days": 30688,
        "temp_c": -195,
        "fact": "Uranus rotates on its side — its axis is tilted nearly 98 degrees!"
    },
    "Neptune": {
        "distance_km": 4_495_100_000,
        "diameter_km": 49_244,
        "moons": 16,
        "day_hours": 16,
        "year_days": 60182,
        "temp_c": -200,
        "fact": "Neptune has the fastest winds in the solar system — up to 2100 km/h!"
    }
}

print("Solar System Explorer")
print("======================")
print("Planets:", ", ".join(planets.keys()))

while True:
    name = input("\nEnter a planet name (or quit): ").strip().title()
    if name.lower() == "quit": break
    if name not in planets:
        print("Planet not found! Try again.")
        continue
    p = planets[name]
    print(f"\n=== {name} ===")
    print(f"  Distance from Sun: {p['distance_km']:,} km")
    print(f"  Diameter:          {p['diameter_km']:,} km")
    print(f"  Moons:             {p['moons']}")
    print(f"  Day length:        {p['day_hours']} hours")
    print(f"  Year length:       {p['year_days']} Earth days")
    print(f"  Avg temperature:   {p['temp_c']}°C")
    print(f"  Fun fact:          {p['fact']}")
