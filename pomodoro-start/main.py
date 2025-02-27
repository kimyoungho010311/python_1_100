import tkinter as tk
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
timer_running = False

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps, timer_running
    reps = 0
    timer_running = False
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
    window.after_cancel(count_down)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps, timer_running
    if timer_running:
        return
    timer_running = True
    reps += 1
    

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #If it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    #If it's the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count // 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        print(count)
        window.after(1000, count_down, count-1)
    else:
        timer_running = False
        start_timer()
        if reps % 2 == 0:
            marks = ""
            work_sessions = math.floor(reps/2)
            for _ in range(work_sessions):
                marks += "✔"
            checkmark.config(text=marks)
        else:
            checkmark.config(text="")       


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tk.Canvas(width=230, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="/Users/kim-youngho/Desktop/python_1_100/pomodoro-start/tomato.png")
canvas.create_image(113, 112, image=tomato_img)
timer_text = canvas.create_text(113, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)



# Label
title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
title_label.grid(row=0, column=1) 

# Button
start_button = tk.Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)  

reset_button = tk.Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

# Checkmark
checkmark = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
checkmark.grid(row=3, column=1)

window.mainloop()