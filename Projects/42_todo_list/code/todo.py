import json
import os
import datetime

FILE = "todos.json"

def load():
    if os.path.exists(FILE):
        with open(FILE) as f:
            return json.load(f)
    return []

def save(todos):
    with open(FILE, "w") as f:
        json.dump(todos, f, indent=2)

def display(todos):
    if not todos:
        print("  (no tasks)")
        return
    for i, t in enumerate(todos):
        done = "✅" if t["done"] else "⬜"
        date = t.get("date", "")
        print(f"  {i+1}. {done} {t['task']} {date}")

todos = load()
print("To-Do List Manager")
print("==================")

while True:
    print(f"\nTasks ({sum(1 for t in todos if not t['done'])} pending):")
    display(todos)
    print("\nCommands: add <task>, done <num>, delete <num>, clear, quit")
    cmd = input("> ").strip().split(maxsplit=1)
    if not cmd: continue
    if cmd[0] == "add" and len(cmd) > 1:
        todos.append({"task": cmd[1], "done": False, "date": datetime.date.today().isoformat()})
        save(todos)
        print(f"Added: {cmd[1]}")
    elif cmd[0] == "done" and len(cmd) > 1:
        try:
            idx = int(cmd[1]) - 1
            todos[idx]["done"] = True
            save(todos)
            print(f"Marked done: {todos[idx]['task']}")
        except (ValueError, IndexError):
            print("Invalid number!")
    elif cmd[0] == "delete" and len(cmd) > 1:
        try:
            idx = int(cmd[1]) - 1
            removed = todos.pop(idx)
            save(todos)
            print(f"Deleted: {removed['task']}")
        except (ValueError, IndexError):
            print("Invalid number!")
    elif cmd[0] == "clear":
        todos = [t for t in todos if not t["done"]]
        save(todos)
        print("Cleared completed tasks!")
    elif cmd[0] == "quit":
        break
print(f"Saved {len(todos)} tasks. Goodbye!")
