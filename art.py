import turtle
turtle.bgcolor = ["black"]
t = turtle.Turtle()
colors = ["red","dark red"]
turtle.speed(200)

for number in range(400):
    t.forward(number)
    t.right(89)
    t.pencolor(colors[number%2])
turtle.done()