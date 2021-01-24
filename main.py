from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text1.config(text="Timer")
    checkmark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    # 2nd, 4th and 6th rep
    if reps % 2 == 0:
        text1.config(text="Rest", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=PINK)
        count_down(short_break_sec)

    elif reps % 8 == 8:
        # 8th rep
        text1.config(text="Break", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=RED)
        count_down(long_break_sec)
    else:
        # 1st, 3rd, 5th and 7th rep
        text1.config(text="Work", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        checkmark.config(text=mark)

    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomelo")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=210, bg=YELLOW, highlightthickness=0)
pomelo_img = PhotoImage(file="grapefruit2.png")
canvas.create_image(104, 102, image=pomelo_img)
timer_text = canvas.create_text(108, 104, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

text1 = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
text1.grid(column=1, row=0)

checkmark = Label(font=(FONT_NAME, 18), bg=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)

button1 = Button(text="Start", font=(FONT_NAME, 8), bg="white", highlightthickness=0, command=start_timer)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", font=(FONT_NAME, 8), bg="white", highlightthickness=0, command=reset_timer)
button2.grid(column=3, row=2)

window.mainloop()


