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


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)


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

checkmark = Label(text="✔", font=(FONT_NAME, 18), bg=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)

button1 = Button(text="Start", font=(FONT_NAME, 8), bg="white", highlightthickness=0, command=start_timer)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", font=(FONT_NAME, 8), bg="white", highlightthickness=0)
button2.grid(column=3, row=2)

window.mainloop()
