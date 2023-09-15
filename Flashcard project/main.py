from tkinter import *
import pandas as pd
import random as rdm

BACKGROUND_COLOR = "#B1DDC6"

def back_card():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=randword["English"], fill="white")


def front_card():
    global to_learn, french_word, flip_timer, randword
    window.after_cancel(flip_timer)
    randword = rdm.choice(to_learn)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=randword["French"], fill="black")
    flip_timer = window.after(3000, back_card)


def remember():
    global remember_word
    to_learn.remove(randword)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    window.after(1, front_card)


def dontremember():
    window.after(1, front_card)
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

flip_timer = window.after(3000, back_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
front_card()
canvas.grid(row=0, column=0, columnspan=2)

rght_btn = Button(
    command=remember, image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0
)
rght_btn.grid(column=1, row=1)
wrng_btn = Button(
    command=dontremember, image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0
)
wrng_btn.grid(column=0, row=1)
window.mainloop()