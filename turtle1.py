import turtle
from turtle import forward, right
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
pen.fillcolor("green")
pen.begin_fill()
pen.circle(100)
pen.end_fill()
turtle.done()
# for making a circle(filled)
for i in range(4):
    forward(50)
    right(90)
    pen.fillcolor("purple")
# for making a square





