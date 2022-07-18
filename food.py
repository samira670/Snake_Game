from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.random()
    def random(self):
        self.goto(random.randint(-278, 280), random.randint(-280, 280))


