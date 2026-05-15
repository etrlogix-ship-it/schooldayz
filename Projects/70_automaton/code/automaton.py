import time, os, random

def clear(): os.system("clear")

ROWS, COLS = 25, 60

def make_grid(random_fill=True):
    if random_fill:
        return [[random.choice([0, 0, 0, 1]) for _ in range(COLS)] for _ in range(ROWS)]
    grid = [[0]*COLS for _ in range(ROWS)]
    # Glider
    coords = [(1,2),(2,3),(3,1),(3,2),(3,3)]
    for r,c in coords: grid[r][c] = 1
    return grid

def count_neighbors(grid, r, c):
    count = 0
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            if dr==0 and dc==0: continue
            nr, nc = (r+dr)%ROWS, (c+dc)%COLS
            count += grid[nr][nc]
    return count

def next_gen(grid):
    new = [[0]*COLS for _ in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            n = count_neighbors(grid, r, c)
            if grid[r][c]:
                new[r][c] = 1 if n in [2,3] else 0
            else:
                new[r][c] = 1 if n == 3 else 0
    return new

def draw(grid, gen):
    clear()
    print(f"Conway's Game of Life — Generation {gen}  (Ctrl+C to stop)")
    chars = ["  ", "██"]
    for row in grid:
        print("".join(chars[c] for c in row))

print("Conway's Game of Life!")
print("======================")
print("1) Random  2) Glider pattern")
choice = input("Choose: ")

grid = make_grid(choice != "2")
gen = 0

try:
    while True:
        draw(grid, gen)
        time.sleep(0.1)
        grid = next_gen(grid)
        gen += 1
except KeyboardInterrupt:
    print(f"\nStopped at generation {gen}")
