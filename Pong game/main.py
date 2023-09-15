from turtle import Screen, Turtle
from paddle import Paddle
from scoreboard import Scoreboard
from pong import Pong
import random
import time

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

scoreboard = Scoreboard()

line = Turtle()
line.color("white")
line.penup()
line.goto(0, 500)
line.setheading(270)
line.pensize(5)
while line.ycor() > -480:
    line.forward(20)
    line.penup()
    line.forward(20)
    line.pendown()

player1 = Paddle((-580, 20))
player2 = Paddle((580, 20))

pong = Pong()
screen.listen()
screen.onkey(fun=player1.up, key="w")
screen.onkey(fun=player1.down, key="s")
screen.onkey(fun=player2.up, key="Up")
screen.onkey(fun=player2.down, key="Down")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.05)
    pong.forward(20)
    pong.move()
    for segmen in player1.paddle:
        if segmen.distance(pong) <= 40:
            pong.setheading(random.randint(270, 450))
            continue
    for segmen in player2.paddle:
        if segmen.distance(pong) <= 40:
            pong.setheading(random.randint(90, 270))
            continue

    if pong.xcor() < -610 or pong.xcor() > 610:
        if pong.xcor() < -580:
            scoreboard.score2 += 1
            pong.setheading(random.randint(270, 450))
        elif pong.xcor() > 580:
            scoreboard.score1 += 1
            pong.setheading(random.randint(90, 270))
        scoreboard.board((-40, 230), scoreboard.score1)
        scoreboard.board((40, 230), scoreboard.score2)
        pong.goto(0, 0)
        player1.posisi_awal(player1.xy)
        player2.posisi_awal(player2.xy)
        time.sleep(0.5)
    is_game_on = scoreboard.winner()


screen.exitonclick()
