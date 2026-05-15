import heapq, time, os

def clear(): os.system("clear")

ROWS, COLS = 15, 30
def heuristic(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(grid, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    visited = set()
    
    while open_set:
        _, current = heapq.heappop(open_set)
        if current in visited: continue
        visited.add(current)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1], visited
        
        r, c = current
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != "#":
                new_g = g_score[current] + 1
                if new_g < g_score.get((nr,nc), float("inf")):
                    g_score[(nr,nc)] = new_g
                    f = new_g + heuristic((nr,nc), goal)
                    came_from[(nr,nc)] = current
                    heapq.heappush(open_set, (f, (nr,nc)))
    return [], visited

import random
grid = [["." if random.random() > 0.25 else "#" for _ in range(COLS)] for _ in range(ROWS)]
start = (0, 0)
goal = (ROWS-1, COLS-1)
grid[0][0] = "S"
grid[ROWS-1][COLS-1] = "E"

def draw(grid, path=set(), visited=set()):
    clear()
    print("A* Pathfinding Visualizer (S=start, E=end, #=wall, ·=path, *=explored)")
    for r, row in enumerate(grid):
        line = ""
        for c, cell in enumerate(row):
            if (r,c) == start: line += "S"
            elif (r,c) == goal: line += "E"
            elif (r,c) in path: line += "·"
            elif (r,c) in visited: line += "*"
            elif cell == "#": line += "█"
            else: line += " "
        print(line)

print("A* Pathfinding Visualizer")
print("=========================")
input("Press Enter to find the path...")

path, explored = astar(grid, start, goal)
path_set = set(path)

for i in range(len(explored)+1):
    draw(grid, path_set if i == len(explored) else set(), set(list(explored)[:i]))
    time.sleep(0.02)

if path:
    print(f"\nPath found! Length: {len(path)} steps")
    print(f"Cells explored: {len(explored)}")
else:
    print("\nNo path found!")
