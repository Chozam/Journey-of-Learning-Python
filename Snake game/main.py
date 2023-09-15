from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.right, key="d")
screen.onkey(fun=snake.left, key="a")


# PR Tambahin event listener ketika layar dipencet akan memulai game
def menu():
    menu = screen.textinput("Play the game", "Start the game (Y/N) : ").upper()
    if menu == "Y":
        return True
    else:
        return False


game_is_on = menu()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        print("nyam nyam")
        scoreboard.score += 1
        scoreboard.board()
        food.pos_food()
        snake.add_segment()

    if (
        snake.head.xcor() <= -290
        or snake.head.xcor() >= 290
        or snake.head.ycor() <= -290
        or snake.head.ycor() >= 290
    ):
        scoreboard.update_high_score()
        snake.reset()
        game_is_on = menu()
        time.sleep(0.5)

    for segmen in snake.segments[1:]:
        if snake.head.distance(segmen) < 10:
            scoreboard.update_high_score()
            snake.reset()
            game_is_on = menu()
            time.sleep(0.5)


print(scoreboard.score)
screen.exitonclick()
