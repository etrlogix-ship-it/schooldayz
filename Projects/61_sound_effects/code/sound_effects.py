import time

effects = {
    "1": ("Explosion",   "💥 BOOM! *rumble* *crackle*"),
    "2": ("Laser",       "⚡ PEEEW! Zzzzap!"),
    "3": ("Rain",        "🌧️  pitter patter pitter patter splash..."),
    "4": ("Crowd cheer", "👥 Yaaaaaaay! *clapping* Wooooo!"),
    "5": ("Cat",         "🐱 Meeoooow... purrrr..."),
    "6": ("Spaceship",   "🚀 Whoooosh... *engine hum* VRRRRM!"),
    "7": ("Thunderclap", "⛈️  KA-BOOOOM! *rumble*"),
    "8": ("Magic spell", "✨ Alakazam! *sparkle* *twinkle*"),
}

print("Sound Effects Machine!")
print("======================")
for num, (name, _) in effects.items():
    print(f"  [{num}] {name}")
print("  [q] Quit")

while True:
    choice = input("\nPlay sound effect: ")
    if choice == "q": break
    if choice in effects:
        name, text = effects[choice]
        print(f"\n{text}")
        time.sleep(0.5)
    else:
        print("Unknown effect!")
print("Thanks for the sound effects!")
