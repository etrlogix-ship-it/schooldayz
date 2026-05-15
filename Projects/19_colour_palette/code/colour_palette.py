import tkinter as tk
import random
import colorsys

def random_palette():
    hue = random.random()
    palette = []
    for i in range(5):
        h = (hue + i * 0.2) % 1.0
        r, g, b = colorsys.hsv_to_rgb(h, 0.8, 0.9)
        hex_color = "#{:02x}{:02x}{:02x}".format(int(r*255), int(g*255), int(b*255))
        palette.append(hex_color)
    return palette

def display_palette():
    for i, color in enumerate(current_palette):
        canvas.itemconfig(rects[i], fill=color)
        labels[i].config(text=color, fg=color)

def new_palette():
    global current_palette
    current_palette = random_palette()
    display_palette()

root = tk.Tk()
root.title("🎨 Colour Palette Maker")
root.geometry("600x300")
root.configure(bg="#1a1a2e")

tk.Label(root, text="🎨 Colour Palette Maker", font=("Arial", 18, "bold"),
         bg="#1a1a2e", fg="white").pack(pady=10)

canvas = tk.Canvas(root, width=550, height=150, bg="#1a1a2e", highlightthickness=0)
canvas.pack()

rects = []
labels_frame = tk.Frame(root, bg="#1a1a2e")
labels_frame.pack()
labels = []

for i in range(5):
    x0 = 10 + i * 110
    rect = canvas.create_rectangle(x0, 10, x0 + 100, 140, fill="#ffffff")
    rects.append(rect)
    lbl = tk.Label(labels_frame, text="#000000", font=("Courier", 10),
                   bg="#1a1a2e", fg="white", width=10)
    lbl.pack(side="left", padx=5)
    labels.append(lbl)

current_palette = []
new_palette()

tk.Button(root, text="✨ New Palette", command=new_palette,
          font=("Arial", 12), bg="#e94560", fg="white",
          padx=20, pady=8).pack(pady=10)

root.mainloop()
