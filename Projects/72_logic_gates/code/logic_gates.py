def AND(a, b): return int(a and b)
def OR(a, b):  return int(a or b)
def NOT(a):    return int(not a)
def XOR(a, b): return int(a != b)
def NAND(a,b): return NOT(AND(a,b))
def NOR(a,b):  return NOT(OR(a,b))

gates = {"AND": AND, "OR": OR, "XOR": XOR, "NAND": NAND, "NOR": NOR}

def truth_table(gate_name, fn, two_inputs=True):
    print(f"\n{gate_name} Gate Truth Table:")
    if two_inputs:
        print("A | B | Output")
        print("--+---+-------")
        for a in [0,1]:
            for b in [0,1]:
                print(f"{a} | {b} |   {fn(a,b)}")
    else:
        print("A | Output")
        print("--+-------")
        for a in [0,1]:
            print(f"{a} |   {fn(a)}")

print("Logic Gates Simulator")
print("=====================")
print("All computers are built from these simple gates!")

while True:
    print("\nGates:", ", ".join(gates.keys()), ", NOT")
    print("Commands: table <gate>, test <gate> <a> <b>, circuit, quit")
    cmd = input("> ").upper().split()
    if not cmd: continue
    if cmd[0] == "TABLE" and len(cmd) > 1:
        g = cmd[1]
        if g == "NOT":
            truth_table("NOT", NOT, False)
        elif g in gates:
            truth_table(g, gates[g])
        else:
            print("Unknown gate!")
    elif cmd[0] == "TEST" and len(cmd) >= 4:
        g = cmd[1]
        try:
            a, b = int(cmd[2]), int(cmd[3])
            if g in gates:
                result = gates[g](a, b)
                print(f"{g}({a},{b}) = {result}")
        except ValueError: print("Use 0 or 1!")
    elif cmd[0] == "CIRCUIT":
        print("\nHalf adder: XOR(A,B) = sum, AND(A,B) = carry")
        for a in [0,1]:
            for b in [0,1]:
                s = XOR(a,b); c = AND(a,b)
                print(f"  {a}+{b} = sum:{s} carry:{c}  ({a+b} in decimal)")
    elif cmd[0] == "QUIT": break
