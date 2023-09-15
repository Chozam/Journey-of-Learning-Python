import pandas as pd
from turtle import Turtle, Screen

data = pd.read_csv("50_states.csv")


screen = Screen()
screen.tracer(0)
screen.title("US STATE GAME")
screen.bgpic("blank_states_img.gif")

kuas = Turtle()
kuas.hideturtle()
kuas.penup()

pensil = Turtle()
pensil.hideturtle()
pensil.penup()
pensil.goto(185, 250)

def scoreboard(score):
    count = len(data.state)
    pensil.clear()
    pensil.write(arg=f"Score: {score}/{count}", font=("Courier", 15, "bold"))
    
score = 0
game_is_on = True
states = []
all_states = data.state.to_list()

scoreboard(score)
while game_is_on:
    screen.update()
    answer = screen.textinput("Country side", "What's the sites: ").title()
    if answer == "Exit":
        # alternative way
        missing_state = [state for state in all_states if state not in states]
        not_answer = pd.DataFrame(missing_state)
        not_answer.to_csv("missing_states.csv")
        break
    if answer in data["state"].unique():
        if answer not in states:
            x = data[data.state == answer].x.item()
            y = data[data.state == answer].y.item()
            kuas.goto(x, y)
            kuas.write(arg=answer.title(), align="center", font=("Courier", 7, "bold"))
            states.append(answer)
            score += 1
            scoreboard(score)
        else:
            continue
    else:
        continue
#alternative way
# for i in states:
#     data.drop(data.index[data.state == i], axis=0, inplace=True)
# data.drop(columns=["x", "y"], inplace=True)
# data = data.reset_index(drop=True)
# not_answer = pd.DataFrame(data)
# not_answer.to_csv("missing_states.csv")
screen.exitonclick()