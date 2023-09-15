import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Road")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.up, key="Up")
screen.onkey(fun=player.down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car_move()
    car_manager.update_location()

    if player.turtle_finish() == True:
        scoreboard.level += 1
        if scoreboard.level < 6:
            scoreboard.update_level()
            car_manager.plus_speed()
        else:
            scoreboard.last_notif("You Win.")
            game_is_on = False

    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.last_notif("GAME OVER.")
            game_is_on = False

screen.exitonclick()
