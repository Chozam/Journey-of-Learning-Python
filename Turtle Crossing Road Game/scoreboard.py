from turtle import Turtle

FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-285, 260)
        self.level = 1
        self.update_level()
    
    def update_level(self):
        self.clear()
        self.write(arg= f"Level: {self.level}", font=FONT)

    def last_notif(self, text):
        self.goto(0,0)
        self.write(arg= text, align= "center", font=FONT)

