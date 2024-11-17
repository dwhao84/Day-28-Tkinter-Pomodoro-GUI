from fileinput import close
from tkinter import *
import time

from PIL.ImageColor import colormap

"""
Spec:
1. Decide on the task to be done
2. Set the timer to 25 mins
3. Work on the task until the timer rings.
4. Take a short 5 min break.
5. Take a 15-30 min break
"""


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down():


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

# 建立title_label的UI，字體顏色(fg)是綠色(GREEN)，背景色(bg)是YELLOW(黃色)，並設定字體。
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png") # 套用PhotoImage的型別，並輸入tomato.png
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

work_label = Label(text="Work")
start_btn = Button(text="Start", highlightthickness=0)
start_btn.grid(column=0, row=2) # 設定start_btn的位置。

reset_btn = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_btn.grid(column=2, row=2) # 設定reset_btn的位置。

check_marks = Label(text="✅", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.tk_setPalette(background=YELLOW)
window.mainloop()