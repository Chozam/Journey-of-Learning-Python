from turtle import Turtle
import random

SPEED = 20

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.setheading(random.randint(0, 360))
        
    
    def move(self):
        if self.ycor()<=-280:
            if self.heading() >= 270 and self.heading() <= 360:
                self.setheading(random.randint(0, 90))
            elif self.heading() >= 180 and self.heading() < 270:
                self.setheading(random.randint(90, 180))
        elif self.ycor()>=280:
            if self.heading() >= 0 and self.heading() < 90:
                self.setheading(random.randint(270, 360))
            elif self.heading() >= 90 and self.heading() < 180:
                self.setheading(random.randint(180, 270))
