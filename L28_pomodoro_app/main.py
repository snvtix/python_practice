import tkinter as tk
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
RED = "#e11a45"
PINK = "#e3afc9"
CREAM = "#efecd7"
YELLOW = "#edc92c"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    reps = 0

    window.after_cancel(timer)

    title_label.config(text="Timer", fg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1

    work_sec = 60 * WORK_MIN
    short_break = 60 * SHORT_BREAK_MIN
    long_break = 60 * LONG_BREAK_MIN

    if reps % 8 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(long_break)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=YELLOW)
        count_down(short_break)
    else:
        title_label.config(text="Work", fg=RED)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=CREAM)

canvas = Canvas(width=200, height=224, bg=CREAM, highlightthickness=0)
tomato = PhotoImage(file="L28_pomodoro_app/tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill=YELLOW, font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1, padx=5, pady=5)

title_label = tk.Label(window, text="Timer", fg=YELLOW, bg=CREAM, font=(FONT_NAME, 35, "bold"))
title_label.grid(row=0, column=1, padx=5, pady=5)

start_button = tk.Button(window, text="Start", fg=RED, bg=PINK, font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=start)
start_button.grid(row=2, column=0, padx=5, pady=5)
reset_button = tk.Button(window, text="Reset", fg=RED, bg=PINK, font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2, padx=5, pady=5)

check_label = tk.Label(window, text="", fg=PINK, bg=CREAM, font=(FONT_NAME, 15, "bold"))
check_label.grid(row=2, column=1, padx=5, pady=5)

window.mainloop()