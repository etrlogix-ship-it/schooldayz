import time

class TrafficLight:
    states = ["RED", "GREEN", "YELLOW"]
    durations = {"RED": 5, "GREEN": 4, "YELLOW": 2}
    transitions = {"RED": "GREEN", "GREEN": "YELLOW", "YELLOW": "RED"}
    icons = {"RED": "🔴", "GREEN": "🟢", "YELLOW": "🟡"}

class VendingMachine:
    def __init__(self):
        self.state = "IDLE"
        self.balance = 0
        self.items = {"crisps": 50, "drink": 120, "chocolate": 80}
    
    def insert(self, amount):
        self.balance += amount
        self.state = "HAS_MONEY"
        print(f"Inserted {amount}p. Balance: {self.balance}p")
    
    def select(self, item):
        if self.state != "HAS_MONEY":
            print("Please insert money first!")
            return
        if item not in self.items:
            print(f"Unknown item! Available: {list(self.items.keys())}")
            return
        price = self.items[item]
        if self.balance >= price:
            self.balance -= price
            print(f"Dispensing {item}! Change: {self.balance}p")
            self.state = "DISPENSING"
            time.sleep(0.5)
            self.balance = 0
            self.state = "IDLE"
        else:
            print(f"{item} costs {price}p. Need {price-self.balance}p more.")
    
    def cancel(self):
        print(f"Returning {self.balance}p")
        self.balance = 0
        self.state = "IDLE"

print("State Machine Simulator")
print("=======================")
print("1) Traffic Light  2) Vending Machine")
choice = input("Choose: ")

if choice == "1":
    tl = TrafficLight()
    state = "RED"
    print("\nPress Ctrl+C to stop the traffic light.")
    try:
        while True:
            icon = tl.icons[state]
            print(f"\r{icon} {state} ({tl.durations[state]}s)  ", end="", flush=True)
            time.sleep(tl.durations[state])
            state = tl.transitions[state]
    except KeyboardInterrupt:
        print("\nLight stopped.")
elif choice == "2":
    vm = VendingMachine()
    print("\nVending Machine! Commands: insert <p>, select <item>, cancel, quit")
    print(f"Items: {vm.items}")
    while True:
        cmd = input("> ").lower().split()
        if not cmd: continue
        if cmd[0] == "insert" and len(cmd) > 1:
            try: vm.insert(int(cmd[1]))
            except ValueError: print("Enter amount in pence!")
        elif cmd[0] == "select" and len(cmd) > 1:
            vm.select(cmd[1])
        elif cmd[0] == "cancel":
            vm.cancel()
        elif cmd[0] == "quit":
            break
