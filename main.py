from turtle import Turtle,colormode,Screen
import random

tim = Turtle()
tim.speed("fastest")
colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
for _ in range (72):
    tim.color(random_color())
    tim.circle(100)
    tim.right(5)
