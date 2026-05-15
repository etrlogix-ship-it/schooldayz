import random

facts = [
    ("Space", "A day on Venus is longer than a year on Venus!"),
    ("Animals", "Octopuses have three hearts and blue blood."),
    ("Physics", "Light takes about 8 minutes to travel from the Sun to Earth."),
    ("Nature", "Honey never spoils — 3000-year-old honey found in Egyptian tombs was still edible."),
    ("Human Body", "The human body contains enough iron to make a small nail."),
    ("Space", "There are more stars in the universe than grains of sand on all Earth beaches."),
    ("Animals", "A group of flamingos is called a flamboyance."),
    ("Physics", "Hot water can freeze faster than cold water — this is called the Mpemba effect."),
    ("Nature", "Trees can communicate with each other through underground fungal networks."),
    ("Human Body", "Your stomach gets a new lining every 3-4 days."),
    ("Space", "Saturn is so light it could float on water (if there was a big enough ocean!)."),
    ("Animals", "Sharks are older than trees. Sharks existed 400 million years ago; trees only 350 million."),
    ("Physics", "Glass is actually a very slow-moving liquid, not a solid."),
    ("Nature", "A single bolt of lightning is five times hotter than the surface of the Sun."),
    ("Human Body", "You have about 37 trillion cells in your body."),
]

print("Science Facts Machine!")
print("======================")
while True:
    category, fact = random.choice(facts)
    print(f"\n[{category}] {fact}")
    if input("\nAnother fact? (yes/no): ").lower() != "yes":
        break
print("Stay curious!")
