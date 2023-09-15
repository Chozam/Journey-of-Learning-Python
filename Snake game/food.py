from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.resizemode("user")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.pos_food()
    
    def pos_food(self):
        koordinatx = random.randint(-27, 27) * 10
        koordinaty = random.randint(-27, 27) * 10
        self.goto(koordinatx, koordinaty)

