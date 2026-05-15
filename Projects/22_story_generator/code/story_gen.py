import random

heroes = ["a brave knight", "a young wizard", "a robot inventor", "a time-travelling cat", "a tiny dragon"]
settings = ["in a magical forest", "on a distant planet", "underwater", "in a floating city"]
problems = ["discovered a hidden treasure", "fought a grumpy giant", "solved an impossible puzzle",
            "befriended a talking rock", "accidentally turned everything purple"]
endings = ["and lived happily ever after", "and learned a very important lesson",
           "and became famous across the land", "and had a great story to tell"]
objects = ["map", "key", "crystal", "hat", "backpack", "robot friend"]
adjectives = ["mysterious", "glowing", "enormous", "tiny", "ancient", "futuristic"]

print("Random Story Generator!")
print("=======================")
print("Press Enter for a new story, Q to quit.")

while True:
    story = (f"Once upon a time, {random.choice(heroes)} was {random.choice(settings)} "
             f"when they {random.choice(problems)}. With the help of a "
             f"{random.choice(adjectives)} {random.choice(objects)}, they overcame the challenge "
             f"-- {random.choice(endings)}!")
    print("\n" + story + "\n")
    cmd = input("Press Enter for another story (or Q to quit): ").strip().lower()
    if cmd == "q":
        break
print("The End!")
