import json, os

FILE = "contacts.json"
def load():
    if os.path.exists(FILE):
        with open(FILE) as f: return json.load(f)
    return {}

def save(c):
    with open(FILE,"w") as f: json.dump(c, f, indent=2)

contacts = load()

print("Contact Book")
print("============")
while True:
    print("\nCommands: add, search, list, delete, quit")
    cmd = input("> ").strip().lower()
    if cmd == "add":
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()
        contacts[name.lower()] = {"name": name, "phone": phone, "email": email}
        save(contacts)
        print(f"Added {name}!")
    elif cmd == "search":
        q = input("Search name: ").lower()
        results = {k:v for k,v in contacts.items() if q in k}
        if results:
            for c in results.values():
                print(f"  {c['name']} | Phone: {c['phone']} | Email: {c['email']}")
        else:
            print("Not found.")
    elif cmd == "list":
        for c in sorted(contacts.values(), key=lambda x: x["name"]):
            print(f"  {c['name']} | {c['phone']} | {c['email']}")
    elif cmd == "delete":
        name = input("Name to delete: ").lower()
        if name in contacts:
            del contacts[name]; save(contacts)
            print(f"Deleted {name}.")
        else:
            print("Not found.")
    elif cmd == "quit":
        break
