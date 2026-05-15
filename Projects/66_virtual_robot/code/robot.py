import os

def clear(): os.system("clear")

GRID = 10
robot = [0, 0]
facing = "E"  # N/E/S/W
grid = [["." for _ in range(GRID)] for _ in range(GRID)]
grid[3][5] = "X"  # obstacle
grid[7][2] = "X"

TURNS_RIGHT = {"N":"E","E":"S","S":"W","W":"N"}
TURNS_LEFT  = {"N":"W","W":"S","S":"E","E":"N"}
MOVES = {"N":(-1,0),"E":(0,1),"S":(1,0),"W":(0,-1)}

def draw():
    clear()
    print("Virtual Robot (R=robot, X=obstacle, .=empty)")
    for r in range(GRID):
        row = ""
        for c in range(GRID):
            if [r,c] == robot:
                arrows = {"N":"↑","E":"→","S":"↓","W":"←"}
                row += arrows[facing]
            elif grid[r][c] == "X":
                row += "X"
            else:
                row += "."
        print(row)
    print(f"Position: {robot} | Facing: {facing}")
    print("Commands: F=forward, L=left, R=right, Q=quit")

draw()
while True:
    cmd = input("> ").upper().strip()
    if cmd == "Q": break
    elif cmd == "L": facing = TURNS_LEFT[facing]
    elif cmd == "R": facing = TURNS_RIGHT[facing]
    elif cmd == "F":
        dr, dc = MOVES[facing]
        nr, nc = robot[0]+dr, robot[1]+dc
        if 0 <= nr < GRID and 0 <= nc < GRID and grid[nr][nc] != "X":
            robot = [nr, nc]
        else:
            print("Blocked!")
    draw()
print("Robot simulation ended!")
