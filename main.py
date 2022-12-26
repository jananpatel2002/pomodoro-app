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
CHECKMARK = "✓"
reps = 0
timer_id = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(
        timer_id)  # Can only cancel a certain ID, so that means we have to set timer_id to (window.after)
    timer_label.config(text="Timer")
    canvas.itemconfig(countdown_text, text=f"00:00")
    checkmark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
# Test comment
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0: # 8th interval
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break")
    elif reps % 2 == 0: # Every 2 intervals
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break")
    else: 
        count_down(WORK_MIN * 60)
        timer_label.config(text="Working")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(minutes):
    rounded_minutes = math.floor(minutes / 60)
    seconds = minutes % 60

    if seconds < 10:
        canvas.itemconfig(countdown_text, text=f"{rounded_minutes}:0{seconds}")
    else:
        canvas.itemconfig(countdown_text, text=f"{rounded_minutes}:{seconds}")
    if minutes >= 0:
        global timer_id
        timer_id = window.after(1000, count_down, minutes - 1)
    else:
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += CHECKMARK
        checkmark.config(text=marks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Window configuration

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas configuration
timer_label = Label()
timer_label.config(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)  # First element all the way at the top

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 111, image=tomato_img)
countdown_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

start_button = Button()
start_button.config(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button()
reset_button.config(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark = Label()
checkmark.config(bg=YELLOW, fg=GREEN, pady=15)
checkmark.grid(row=3, column=1)

window.mainloop()
