from tkinter import *
import math
#----------------------- CONSTANTS -------------------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
#--------------------------- TIMER RESET----------------------#
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text,text = "00:00")
    check_mark.config(text="")
#--------------------------- TIMER MECHANISM ----------------------#
def start_timer():
    
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_min)
        timer_label.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work",fg=GREEN)
        
        
        
   
#--------------------------- COUNTDOWN MECHANISM ----------------------#
 
def count_down(count):
    global timer
    count_min =  math.floor(count / 60)
    count_sec = count % 60 
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
       timer = window.after(1000, count_down,count - 1)
    else:
        start_timer()
        check = ""
        for _ in range(math.floor(reps/2)) :
            check += "V"
            check_mark.config(text=check)

#--------------------------- UI SETUP ----------------------#

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

timer_label = Label(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(column=1,row=0)

tomato_img = PhotoImage(file="/home/carlos/Bureau/100 days of python/Day 28/Tomato.png")
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,120,image=tomato_img)
timer_text = canvas.create_text(100,150,text="00:00",fill="white",font=(FONT_NAME,25,"bold"))
canvas.grid(column=1,row=1)
start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)
check_mark = Label(fg=GREEN,background=YELLOW)
check_mark.grid(column=1,row=3)
reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)












window.mainloop()