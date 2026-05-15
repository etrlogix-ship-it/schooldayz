import tkinter as tk

def update_color(*args):
    r = int(r_var.get())
    g = int(g_var.get())
    b = int(b_var.get())
    hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    color_box.config(bg=hex_color)
    hex_label.config(text="Hex: " + hex_color.upper())
    rgb_label.config(text="RGB: ({}, {}, {})".format(r, g, b))

root = tk.Tk()
root.title("Colour Mixing Lab")
root.configure(bg="#1a1a2e")

tk.Label(root, text="Colour Mixing Lab", font=("Arial", 18, "bold"),
         bg="#1a1a2e", fg="white").pack(pady=10)
color_box = tk.Label(root, width=30, height=8, bg="#000000")
color_box.pack(pady=10)
hex_label = tk.Label(root, text="Hex: #000000", font=("Courier", 14), bg="#1a1a2e", fg="white")
hex_label.pack()
rgb_label = tk.Label(root, text="RGB: (0, 0, 0)", font=("Courier", 12), bg="#1a1a2e", fg="white")
rgb_label.pack(pady=5)

sliders_frame = tk.Frame(root, bg="#1a1a2e")
sliders_frame.pack(pady=10)
r_var = tk.DoubleVar()
g_var = tk.DoubleVar()
b_var = tk.DoubleVar()
for label, var in [("Red", r_var), ("Green", g_var), ("Blue", b_var)]:
    row = tk.Frame(sliders_frame, bg="#1a1a2e")
    row.pack(fill="x", padx=20, pady=3)
    tk.Label(row, text=label, width=8, bg="#1a1a2e", fg="white", font=("Arial", 11)).pack(side="left")
    tk.Scale(row, from_=0, to=255, orient="horizontal", variable=var,
             command=update_color, length=300, bg="#2d2d2d", fg="white").pack(side="left")

root.mainloop()
