from tkinter import *
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = NONE
reps = 1
checks = ""


# ------- TIMER RESET ------- #
def reset_timer():
    global timer
    global reps
    global checks
    window.after_cancel(timer)
    reps = 1
    checks = ""
    label.config(text="Timer", font=("Consolas", 38), bg=YELLOW, fg=GREEN)
    check_rounds.config(text="", bg=YELLOW, fg="#299900")
    canvas.itemconfig(timer_text, text=f"Focus!")


# ------- TIMER MECHANISM ------- #

def start_clicked():
    global reps
    global checks
    if len(checks) % 10 == 0:
        checks += "\n"
    work_sec = 60 * WORK_MIN
    short_sec = 60 * SHORT_BREAK_MIN
    long_sec = 60 * LONG_BREAK_MIN

    if reps % 2 != 0:
        seconds = work_sec
        label.config(text="Work!", font=("Consolas", 38), bg=YELLOW, fg=GREEN)
    elif reps % 8 == 0:
        seconds = long_sec
        label.config(text="Break!", font=("Consolas", 38), bg=YELLOW, fg=RED)

    else:
        seconds = short_sec
        label.config(text="Break!", font=("Consolas", 38), bg=YELLOW, fg=PINK)

    count_down(seconds)


# ------- COUNTDOWN MECHANISM ------- #
def count_down(count):
    global reps
    global checks
    global timer

    count_minute = count // 60
    if count_minute < 10:
        count_minute = f"0{count_minute}"

    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"

    if count_minute == "00" and count_second == "00":
        reps += 1
        print('\a')
        winsound.Beep(2500, 1000)     # or print("\a") in other OSs
        if reps % 2 == 0:
            checks += "✅"
            check_rounds.config(text=checks, bg=YELLOW, fg="#299900")
        start_clicked()
    else:
        canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
        timer = window.after(1000, count_down, count - 1)


# ------- UI SETUP ------- #
window = Tk()
window.title("Pomodoro Technique")
window.minsize(300, 300)
window.config(padx=100, pady=50, bg=YELLOW)
window.eval('tk::PlaceWindow . center')

label = Label(text="Timer", font=("Consolas", 38), bg=YELLOW, fg=GREEN)
label.grid(column=1, row=0)

canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=tomato_img)
timer_text = canvas.create_text(158, 180, text="Focus!", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", width=5, highlightthickness=0, command=start_clicked)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=5, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_rounds = Label(bg=YELLOW, fg="#299900")
check_rounds.grid(column=1, row=3)

window.mainloop()
