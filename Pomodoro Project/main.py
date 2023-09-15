from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
alternate = 0
check = ""
after = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global after, alternate
    window.after_cancel(after)
    pomodoro.config(text="POMODORO", fg="white")
    canvas.itemconfig(tim, text="25:00")
    checklist.config(text="")
    alternate = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer():
    global alternate, check
    short_break_second = SHORT_BREAK_MIN * 60
    long_break_second = LONG_BREAK_MIN * 60
    work_min_second = WORK_MIN * 60
    alternate += 1
    if alternate % 8 == 0:
        pomodoro.config(text="BREAK", fg=RED)
        check += "✅"
        checklist.config(text=check)
        countdown(long_break_second)
    elif alternate % 2 == 1:
        pomodoro.config(text="FOCUS", fg=GREEN)
        countdown(work_min_second)
    elif alternate % 2 == 0:
        pomodoro.config(text="BREAK", fg=YELLOW)
        check += "✅"
        checklist.config(text=check)
        countdown(short_break_second)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(time):
    minute = math.floor(time/60)
    second = time % 60
    if minute < 10 and second < 10:
        canvas.itemconfig(tim, text=f"0{minute}:0{second}")
    elif minute < 10:
        canvas.itemconfig(tim, text=f"0{minute}:{second}")
    elif second < 10:
        canvas.itemconfig(tim, text=f"{minute}:0{second}")
    else:
        canvas.itemconfig(tim, text=f"{minute}:{second}")
    if time > 0:
        global after
        after = window.after(1000, countdown, time - 1)
    else:
        timer()
# def countdown(min=WORK_MIN):
#     min = WO
#     if min == 0 and sec == 0:
#         canvas.itemconfig(tim, text=f"{min}:{sec}")
#     elif sec == 0:
#         canvas.itemconfig(tim, text=f"{min}:00")
#         window.after(10, countdown, min - 1, sec + 59)
#     elif sec < 10:
#         canvas.itemconfig(tim, text=f"{min}:0{sec}")
#         window.after(10, countdown, min, sec-1)
#     else:
#         canvas.itemconfig(tim, text=f"{min}:{sec}")
#         window.after(10, countdown, min, sec-1)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=PINK)
tomato = PhotoImage(file="tomato.png")
pomodoro = Label(text="POMODORO", bg=PINK, fg="white", font=(FONT_NAME, 35, "bold"))
pomodoro.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=PINK, bd=0, highlightthickness=0)
image_tomato = canvas.create_image(100, 112, image= tomato)
tim = canvas.create_text(105, 130, text="25:00", font=(FONT_NAME, 35, "bold"), fill=YELLOW)
canvas.grid(row=1, column=1, pady=20)
start_button = Button(command=timer, text="start", fg="white", font=(FONT_NAME, 15, "bold"), bg=RED)
start_button.grid(row=3, column=0)
checklist = Label(bg=PINK, fg=GREEN)
checklist.grid(row=3, column=1)
reset_button = Button(command=reset, text="reset", fg="white", font=(FONT_NAME, 15, "bold"), bg=RED)
reset_button.grid(row=3, column=2)

window.mainloop()