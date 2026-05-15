import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🐢 Turtle Art!")
t.speed(10)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink", "white"]

def draw_star(size, color):
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def draw_spiral():
    t.pencolor("white")
    for i in range(200):
        t.forward(i * 0.5)
        t.right(91)
        t.pencolor(colors[i % len(colors)])

def draw_flower():
    for _ in range(36):
        t.color(random.choice(colors))
        t.circle(80)
        t.right(10)

print("Choose a drawing:")
print("1) Spiral  2) Stars  3) Flower")
choice = input("Choice: ")

if choice == "1":
    draw_spiral()
elif choice == "2":
    for _ in range(20):
        t.penup()
        t.goto(random.randint(-300, 300), random.randint(-200, 200))
        t.pendown()
        draw_star(random.randint(20, 80), random.choice(colors))
elif choice == "3":
    draw_flower()
else:
    draw_spiral()

screen.mainloop()
