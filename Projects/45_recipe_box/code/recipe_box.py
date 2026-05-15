import json, os

FILE = "recipes.json"
def load():
    if os.path.exists(FILE):
        with open(FILE) as f: return json.load(f)
    return {}
def save(r):
    with open(FILE,"w") as f: json.dump(r, f, indent=2)

recipes = load()

print("Recipe Box")
print("==========")
while True:
    print("\nCommands: add, view, list, search, delete, quit")
    cmd = input("> ").strip().lower()
    if cmd == "add":
        name = input("Recipe name: ").strip()
        servings = input("Servings: ").strip()
        print("Enter ingredients (one per line, blank to stop):")
        ingredients = []
        while True:
            ing = input("  > ").strip()
            if not ing: break
            ingredients.append(ing)
        print("Enter instructions (one step per line, blank to stop):")
        steps = []
        while True:
            step = input(f"  Step {len(steps)+1}: ").strip()
            if not step: break
            steps.append(step)
        recipes[name.lower()] = {"name": name, "servings": servings,
                                  "ingredients": ingredients, "steps": steps}
        save(recipes)
        print(f"Saved recipe: {name}!")
    elif cmd == "view":
        name = input("Recipe name: ").lower()
        if name in recipes:
            r = recipes[name]
            print(f"\n{r['name']} (serves {r['servings']})")
            print("Ingredients:")
            for ing in r["ingredients"]: print(f"  - {ing}")
            print("Instructions:")
            for i, step in enumerate(r["steps"], 1): print(f"  {i}. {step}")
        else:
            print("Recipe not found!")
    elif cmd == "list":
        for r in sorted(recipes.values(), key=lambda x: x["name"]):
            print(f"  {r['name']} (serves {r['servings']})")
    elif cmd == "search":
        q = input("Search: ").lower()
        found = [r for r in recipes.values() if q in r["name"].lower()]
        if found:
            for r in found: print(f"  {r['name']}")
        else:
            print("Nothing found.")
    elif cmd == "delete":
        name = input("Recipe to delete: ").lower()
        if name in recipes:
            del recipes[name]; save(recipes); print("Deleted!")
        else:
            print("Not found.")
    elif cmd == "quit":
        break
