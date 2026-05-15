import json, os, datetime

FILE = "budget.json"
def load():
    if os.path.exists(FILE):
        with open(FILE) as f: return json.load(f)
    return []

def save(data):
    with open(FILE,"w") as f: json.dump(data, f, indent=2)

transactions = load()

def balance():
    return sum(t["amount"] for t in transactions)

print("Pocket Money Tracker")
print("====================")

while True:
    print(f"\nCurrent balance: £{balance():.2f}")
    print("Commands: add <amount> <description>, list, quit")
    print("  (use + for income e.g. +5 Birthday money, - for spending e.g. -2.50 Sweets)")
    cmd = input("> ").strip().split(maxsplit=1)
    if not cmd: continue
    if cmd[0] == "add" and len(cmd) > 1:
        parts = cmd[1].split(maxsplit=1)
        try:
            amount = float(parts[0])
            desc = parts[1] if len(parts) > 1 else "?"
            transactions.append({"amount": amount, "desc": desc,
                                  "date": datetime.date.today().isoformat()})
            save(transactions)
            print(f"Recorded: £{amount:+.2f} — {desc}")
        except (ValueError, IndexError):
            print("Usage: add +5 Birthday money OR add -2.50 Sweets")
    elif cmd[0] == "list":
        for t in transactions[-10:]:
            symbol = "+" if t["amount"] >= 0 else ""
            print(f"  {t['date']} {symbol}£{t['amount']:.2f}  {t['desc']}")
    elif cmd[0] == "quit":
        break
