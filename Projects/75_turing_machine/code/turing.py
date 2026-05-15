print("Turing Machine Simulator")
print("=========================")
print("A Turing machine has: tape, read/write head, state, transition rules.")
print("This simulates incrementing a binary number.\n")

class TuringMachine:
    def __init__(self, tape, rules, start="q0", accept="qA", reject="qR"):
        self.tape = list(tape) + ["_"] * 20
        self.head = 0
        self.state = start
        self.accept = accept
        self.reject = reject
        self.rules = rules
        self.steps = 0
    
    def show(self):
        tape_str = "".join(self.tape[:20])
        head_str = " " * self.head + "^"
        print(f"State: {self.state:5} | ...{tape_str}...")
        print(f"                  ...{head_str}...")
    
    def step(self):
        sym = self.tape[self.head]
        key = (self.state, sym)
        if key not in self.rules:
            self.state = self.reject
            return False
        new_state, write, move = self.rules[key]
        self.tape[self.head] = write
        self.state = new_state
        self.head += 1 if move == "R" else -1
        self.head = max(0, self.head)
        self.steps += 1
        return True

# Increment binary number
rules = {
    ("q0","1"): ("q0","1","R"),
    ("q0","0"): ("q0","0","R"),
    ("q0","_"): ("q1","_","L"),
    ("q1","1"): ("q1","0","L"),
    ("q1","0"): ("qA","1","R"),
    ("q1","_"): ("qA","1","R"),
}

tape = input("Enter binary number (e.g. 1011): ").strip() or "1011"
print(f"\nIncrementing binary {tape}...")
tm = TuringMachine(tape, rules)

import time
while tm.state not in [tm.accept, tm.reject] and tm.steps < 100:
    tm.show()
    time.sleep(0.3)
    tm.step()

print(f"\nResult: {''.join(tm.tape).rstrip('_')}")
print(f"Steps taken: {tm.steps}")
expected = bin(int(tape, 2) + 1)[2:]
print(f"Expected:    {expected}")
