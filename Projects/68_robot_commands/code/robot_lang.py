import os, time

def clear(): os.system("clear")

SIZE = 12
robot = {"x": 0, "y": 0, "dir": 0}  # dir: 0=N,1=E,2=S,3=W
trail = set()

MOVES = [(0,-1),(1,0),(0,1),(-1,0)]  # N,E,S,W
DIR_NAMES = ["N","E","S","W"]

def draw():
    clear()
    arrows = ["↑","→","↓","←"]
    print("Robot World")
    for y in range(SIZE):
        row = ""
        for x in range(SIZE):
            if robot["x"] == x and robot["y"] == y:
                row += arrows[robot["dir"]]
            elif (x,y) in trail:
                row += "·"
            else:
                row += "."
        print(row)
    print(f"Pos: ({robot['x']},{robot['y']}) Dir: {DIR_NAMES[robot['dir']]}")

def run_program(code):
    lines = code.strip().split("\n")
    for line in lines:
        parts = line.strip().split()
        if not parts: continue
        cmd = parts[0].upper()
        
        if cmd == "FORWARD":
            n = int(parts[1]) if len(parts) > 1 else 1
            for _ in range(n):
                dx, dy = MOVES[robot["dir"]]
                nx, ny = robot["x"]+dx, robot["y"]+dy
                if 0 <= nx < SIZE and 0 <= ny < SIZE:
                    trail.add((robot["x"], robot["y"]))
                    robot["x"], robot["y"] = nx, ny
        elif cmd == "RIGHT":
            robot["dir"] = (robot["dir"] + 1) % 4
        elif cmd == "LEFT":
            robot["dir"] = (robot["dir"] - 1) % 4
        elif cmd == "REPEAT":
            count = int(parts[1])
            # Find matching END
            pass  # simplified
        draw()
        time.sleep(0.3)

print("Robot Command Language!")
print("=======================")
print("Commands: FORWARD [n], RIGHT, LEFT")
print("Example program:")
print("  FORWARD 3")
print("  RIGHT")
print("  FORWARD 3")
print("  LEFT")
print("(Type END on a new line to run)")

draw()
lines = []
print("\nEnter program:")
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

run_program("\n".join(lines))
print("\nProgram finished!")
