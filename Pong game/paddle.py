from turtle import Turtle

STARTING_POINT = [(0, 20), (0, 0), (0, -20)]
SPEED = 50


class Paddle:
    def __init__(self, koor):
        self.paddle = []
        for position in STARTING_POINT:
            segmen = Turtle()
            segmen.color("white")
            segmen.shape("square")
            segmen.penup()
            segmen.goto(position)
            self.paddle.append(segmen)
        self.head = self.paddle[0]
        self.tail = self.paddle[2]
        self.xy = koor
        self.posisi_awal(koor)

    def posisi_awal(self, koor):
        self.head.goto(koor)
        self.follow_paddle()

    def follow_paddle(self):
        self.paddle[1].goto(self.paddle[0].xcor(), self.paddle[0].ycor() - 20)
        self.paddle[2].goto(self.paddle[1].xcor(), self.paddle[1].ycor() - 20)

    def up(self):
        self.head.setheading(90)
        if self.head.ycor() <= 270:
            self.head.fd(SPEED)
            self.follow_paddle()

    def down(self):
        self.head.setheading(270)
        if self.tail.ycor() >= -270:
            self.head.fd(SPEED)
            self.follow_paddle()
