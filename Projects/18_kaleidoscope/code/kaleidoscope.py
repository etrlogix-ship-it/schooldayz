import turtle
import random
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🌈 Kaleidoscope")
screen.tracer(0)

pens = []
num_pens = 6
for i in range(num_pens):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    pens.append(t)

angle_step = 360 / num_pens
hue = 0

for step in range(400):
    hue = (hue + 0.005) % 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    color = (r, g, b)

    for i, pen in enumerate(pens):
        pen.color(color)
        pen.setheading(i * angle_step + step)
        pen.forward(step * 0.3)
        pen.right(91)

    if step % 20 == 0:
        screen.update()

screen.update()
print("Press Ctrl+C to close the window.")
turtle.done()
