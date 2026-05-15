data = {
    "animals": {
        "Blue Whale": "The largest animal ever known to have existed, up to 30m long.",
        "Platypus": "One of the few mammals that lay eggs. Males have venomous spurs!",
        "Mantis Shrimp": "Can punch with the force of a bullet and see 16 types of colour!",
        "Tardigrade": "A microscopic animal that can survive in space, volcanoes, and deep sea.",
        "Axolotl": "A salamander that never fully metamorphoses and can regrow limbs!",
    },
    "countries": {
        "Iceland": "Has no standing army and uses 100% renewable energy!",
        "Japan": "Has the world\'s oldest company, Kongo Gumi, founded in 578 AD.",
        "Brazil": "Home to 60% of the Amazon rainforest.",
        "New Zealand": "First country to give women the right to vote in 1893.",
        "Norway": "Penguins in the Oslo zoo are given military rank!",
    },
    "inventions": {
        "Internet": "Created by Tim Berners-Lee in 1989 as a way to share research.",
        "Velcro": "Inspired by how burr seeds stuck to a dog\'s fur in 1941.",
        "Post-it Note": "Invented by accident when a scientist made a glue that didn\'t stick well.",
        "Penicillin": "Discovered by Alexander Fleming who noticed mould killing bacteria.",
        "X-ray": "Wilhelm Roentgen discovered X-rays accidentally in 1895.",
    }
}

print("Pocket Encyclopedia")
print("===================")
while True:
    print("\nCategories:", ", ".join(data.keys()))
    cat = input("Choose category (or quit): ").lower().strip()
    if cat == "quit": break
    if cat in data:
        print(f"\nTopics in {cat}:")
        for topic in data[cat]:
            print(f"  - {topic}")
        topic = input("\nChoose topic: ").strip()
        topic_key = next((k for k in data[cat] if k.lower() == topic.lower()), None)
        if topic_key:
            print(f"\n{topic_key}:")
            print(f"  {data[cat][topic_key]}")
        else:
            print("Topic not found!")
    else:
        print("Category not found!")
