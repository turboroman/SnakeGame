from turtle import Turtle
from random import randint
SIZE = 0.6


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(SIZE, SIZE)
        self.color('green')
        self.speed(10)
        self.refresh()

    def refresh(self):
        self.goto(randint(-280, 280), randint(-280, 280))
