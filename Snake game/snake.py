from turtle import Turtle

STARTING_POSITION =[(0, 0), (-20, 0), (-40, 0)]
PACE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.speed = PACE
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        for position in STARTING_POSITION:
            self.karakteristik(position)

    def reset(self):
        for segmen in self.segments:
            segmen.ht()
        self.speed = 0
        self.segments.clear()
        self.make_snake()
        self.head = self.segments[0]
        self.speed = PACE

    def karakteristik(self, position):
        my_snake = Turtle("square")
        self.color = my_snake.color("white")
        self.penmode = my_snake.penup()
        self.place_segment = my_snake.goto(position)
        self.segments.append(my_snake)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(self.speed)
    

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def add_segment(self):
        posisi = self.segments[-1].position()
        self.karakteristik(posisi)


