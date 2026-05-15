import tkinter as tk
from tkinter import colorchooser

GRID_SIZE = 20
CELL = 25

class PixelArt:
    def __init__(self, root):
        self.root = root
        root.title("Pixel Art Maker")
        self.color = "#ff0000"

        toolbar = tk.Frame(root, bg="#222", pady=5)
        toolbar.pack(fill="x")
        tk.Label(toolbar, text="Pixel Art", font=("Arial", 12, "bold"),
                 bg="#222", fg="white").pack(side="left", padx=10)
        tk.Button(toolbar, text="Pick Colour", command=self.pick_color,
                  bg="#555", fg="white").pack(side="left", padx=3)
        for c in ["#ff0000","#ff8800","#ffff00","#00cc00","#0088ff","#8800ff","#ffffff","#000000"]:
            tk.Button(toolbar, bg=c, width=2, command=lambda col=c: self.set_color(col)).pack(side="left", padx=1)
        tk.Button(toolbar, text="Clear", bg="#e94560", fg="white",
                  command=self.clear).pack(side="left", padx=5)

        self.canvas = tk.Canvas(root, width=GRID_SIZE*CELL, height=GRID_SIZE*CELL)
        self.canvas.pack(padx=10, pady=10)
        self.cells = {}
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                x0, y0 = c*CELL, r*CELL
                rect = self.canvas.create_rectangle(x0, y0, x0+CELL, y0+CELL,
                                                    fill="white", outline="#ddd")
                self.cells[(r,c)] = rect
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<Button-1>", self.draw)

    def set_color(self, c): self.color = c
    def pick_color(self):
        c = colorchooser.askcolor()[1]
        if c: self.color = c

    def draw(self, event):
        c, r = event.x // CELL, event.y // CELL
        if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
            self.canvas.itemconfig(self.cells[(r,c)], fill=self.color)

    def clear(self):
        for rect in self.cells.values():
            self.canvas.itemconfig(rect, fill="white")

root = tk.Tk()
PixelArt(root)
root.mainloop()
