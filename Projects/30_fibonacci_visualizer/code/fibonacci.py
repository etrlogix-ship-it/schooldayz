import tkinter as tk
import math

def fibonacci_sequence(n):
    seq = [0, 1]
    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq

root = tk.Tk()
root.title("Fibonacci Visualizer")
root.configure(bg="#1a1a2e")

tk.Label(root, text="Fibonacci Sequence", font=("Arial", 16, "bold"),
         bg="#1a1a2e", fg="#e94560").pack(pady=5)

canvas = tk.Canvas(root, width=700, height=400, bg="#0f3460")
canvas.pack(padx=10, pady=10)

n_var = tk.IntVar(value=10)

def draw():
    canvas.delete("all")
    n = n_var.get()
    seq = fibonacci_sequence(n)
    
    # Draw bars
    max_val = max(seq[1:]) if len(seq) > 1 else 1
    bar_w = 680 // n
    colors = ["#e94560", "#f5a623", "#7ed321", "#4a90e2", "#bd10e0"]
    
    for i, val in enumerate(seq):
        height = int((val / max_val) * 350) if max_val > 0 else 0
        x0 = 10 + i * bar_w
        y0 = 390 - height
        color = colors[i % len(colors)]
        canvas.create_rectangle(x0, y0, x0 + bar_w - 2, 390, fill=color)
        if bar_w > 20:
            canvas.create_text(x0 + bar_w//2, 390 - height - 10,
                               text=str(val), fill="white", font=("Arial", 8))
    
    # Show sequence
    seq_str = " → ".join(map(str, seq))
    canvas.create_text(350, 10, text=seq_str[:80], fill="#aaa", font=("Courier", 9))

frame = tk.Frame(root, bg="#1a1a2e")
frame.pack()
tk.Label(frame, text="Terms:", bg="#1a1a2e", fg="white").pack(side="left")
tk.Scale(frame, from_=3, to=20, orient="horizontal", variable=n_var,
         command=lambda e: draw(), bg="#2d2d2d", fg="white", length=200).pack(side="left")

draw()
root.mainloop()
