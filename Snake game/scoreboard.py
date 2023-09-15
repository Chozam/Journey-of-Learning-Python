from turtle import Turtle

FONT = ("Courier", 17, "bold")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_file()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.board()

    def board(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGN,
            font=FONT,
        )

    def update_high_score(self):
        if self.high_score < self.score:
            self.save_score(self.score)
            self.read_file()
        self.score = 0
        self.board()

    def read_file(self):
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())

    def save_score(self, score):
        with open("high_score.txt", mode="w") as file:
            file.write(str(score))
