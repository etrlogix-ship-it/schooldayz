import random, os, time

def clear(): os.system("clear")

def generate_maze(rows, cols):
    maze = [["#"] * (cols*2+1) for _ in range(rows*2+1)]
    visited = [[False]*cols for _ in range(rows)]
    
    def carve(r, c):
        visited[r][c] = True
        maze[r*2+1][c*2+1] = " "
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        random.shuffle(dirs)
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                maze[r*2+1+dr][c*2+1+dc] = " "
                carve(nr, nc)
    
    carve(0, 0)
    maze[1][0] = "S"
    maze[rows*2-1][cols*2] = "E"
    return maze

def solve_maze(maze):
    rows = len(maze)
    cols = len(maze[0])
    start = (1, 1)
    end = (rows-2, cols-2)
    
    stack = [start]
    came_from = {start: None}
    
    while stack:
        pos = stack.pop()
        if pos == end:
            path = []
            while pos:
                path.append(pos)
                pos = came_from[pos]
            return path[::-1]
        r, c = pos
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r+dr, c+dc
            if (nr, nc) not in came_from and 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != "#":
                came_from[(nr,nc)] = pos
                stack.append((nr,nc))
    return []

def print_maze(maze, path=None, current=None):
    clear()
    for r, row in enumerate(maze):
        line = ""
        for c, cell in enumerate(row):
            if current and (r,c) == current:
                line += "●"
            elif path and (r,c) in path:
                line += "·"
            else:
                line += cell
        print(line)

print("Maze Generator & Solver!")
print("========================")
try:
    size = int(input("Maze size (5-15, default 8): ") or "8")
    size = max(5, min(15, size))
except ValueError:
    size = 8

maze = generate_maze(size, size)
print_maze(maze)
input("\nPress Enter to solve...")

path = solve_maze(maze)
path_set = set(path)
print_maze(maze, path_set)
print(f"\nSolved! Path length: {len(path)} steps")
input("Press Enter to animate...")

for i, pos in enumerate(path):
    print_maze(maze, set(path[:i+1]), pos)
    time.sleep(0.1)
print("\nMaze solved!")
