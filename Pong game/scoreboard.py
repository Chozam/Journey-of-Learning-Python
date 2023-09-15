from turtle import Turtle

FONT = ("Courier", 40, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.board((-40, 230), self.score1)
        self.board((40, 230), self.score2)

    def board(self, position, score):
        self.clear()
        self.goto(position)
        self.write(arg=f"{score}", align="center", font=FONT)

    def winner(self):
        if self.score1 == 5:
            self.goto(0, 0)
            self.write(
                arg="      GAME OVER.\nPLAYER 1 WIN THE GAME.",
                align="center",
                font=FONT,
            )
            return False
        elif self.score2 == 5:
            self.goto(0, 0)
            self.write(
                arg="      GAME OVER.\nPLAYER 2 WIN THE GAME.",
                align="center",
                font=FONT,
            )
            return False
        return True
