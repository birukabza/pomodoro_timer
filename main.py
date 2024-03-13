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
reps = 0
time = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(text_timer, text="00:00")
    title_label.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN*60
    short_break_sec= SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps%8 ==0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
            check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("The Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)
window.minsize(width=600, height=600)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 70))
title_label.grid(column=1, row=0)

canvas = Canvas(width=500, height=500, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="animated_tomato-removebg-preview.png")
canvas.create_image(250, 250, image=tomato_img)
text_timer = canvas.create_text(265, 350, text="00:00", font=(FONT_NAME, 50, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, font=(40), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, font=(40), command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()
