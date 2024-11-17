import math
from tkinter import *
import time

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
reps = 0
timer = None #  表示計時器尚未開始


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    # 在取消計時器之前先檢查它是否存在
    if timer is not None:  # 新增這個檢查
        window.after_cancel(timer)
        timer = None  # 計時器取消後，將狀態重置
    
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=RED)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # Dynamic Data type，C語言是沒辦法這樣的，例如:Swift、C。
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    print(count)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)  # ms:毫秒, call function,
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✅"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

# 建立title_label的UI，字體顏色(fg)是綠色(GREEN)，背景色(bg)是YELLOW(黃色)，並設定字體。
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # 套用PhotoImage的型別，並輸入tomato.png
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)  # 加上start_time的function。
start_btn.grid(column=0, row=2)  # 設定start_btn的位置。

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)  # 設定reset_btn的位置。

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.tk_setPalette(background=YELLOW)
window.mainloop()