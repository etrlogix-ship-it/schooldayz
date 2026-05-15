import tkinter as tk
from tkinter import colorchooser, messagebox
import datetime

class GraffitiWall:
    def __init__(self, root):
        self.root = root
        self.root.title("🎨 Digital Graffiti Wall")
        self.color = "#ff0000"
        self.size = 10
        self.last_x = self.last_y = None

        toolbar = tk.Frame(root, bg="#2d2d2d", pady=5)
        toolbar.pack(fill="x")

        tk.Label(toolbar, text="🎨 Graffiti Wall", font=("Arial", 14, "bold"),
                 bg="#2d2d2d", fg="white").pack(side="left", padx=10)

        tk.Button(toolbar, text="Choose Colour", command=self.pick_color,
                  bg="#4a4a4a", fg="white").pack(side="left", padx=5)

        self.size_var = tk.IntVar(value=10)
        tk.Scale(toolbar, from_=2, to=50, orient="horizontal", label="Size",
                 variable=self.size_var, bg="#2d2d2d", fg="white",
                 length=100).pack(side="left", padx=5)

        for clr in ["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff", "#ffffff", "#000000"]:
            b = tk.Button(toolbar, bg=clr, width=2, command=lambda c=clr: self.set_color(c))
            b.pack(side="left", padx=2)

        tk.Button(toolbar, text="Clear", command=self.clear,
                  bg="#e94560", fg="white").pack(side="left", padx=5)
        tk.Button(toolbar, text="Save", command=self.save,
                  bg="#2ecc71", fg="white").pack(side="left", padx=5)

        self.canvas = tk.Canvas(root, bg="black", cursor="crosshair")
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def set_color(self, c): self.color = c
    def pick_color(self):
        c = colorchooser.askcolor()[1]
        if c: self.color = c

    def paint(self, event):
        size = self.size_var.get()
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    fill=self.color, width=size, capstyle="round",
                                    smooth=True, splinesteps=36)
        self.last_x, self.last_y = event.x, event.y

    def reset(self, event): self.last_x = self.last_y = None

    def clear(self):
        if messagebox.askyesno("Clear?", "Erase everything?"):
            self.canvas.delete("all")

    def save(self):
        name = f"graffiti_{datetime.datetime.now().strftime('%H%M%S')}.ps"
        self.canvas.postscript(file=name, colormode="color")
        messagebox.showinfo("Saved!", f"Saved as {name}")

root = tk.Tk()
root.geometry("900x600")
GraffitiWall(root)
root.mainloop()
