import time
from datetime import datetime
from plyer import notification
import tkinter as tk
import customtkinter as ct
import winsound

def update_current_time():
    current_time = datetime.now().strftime("%I:%M:%S")
    l1.configure(text=f"Current time: {current_time}")
    r.after(1, update_current_time)  # Update every 1000 milliseconds (1 second)

def start_countdown(countdown_time):
    if countdown_time < 0:
        notification.notify(title="Invalid Time", message="Please enter a valid countdown time.", timeout=5)

    mins, secs = divmod(countdown_time, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    l2.configure(text=f"Countdown: {timer}")

    if countdown_time > 0:
        r.after(1000, start_countdown, countdown_time - 1)

    if countdown_time == 0:
        notification.notify(title="Countdown Complete", message="Time's up!", timeout=10)
        # Play sound when countdown is complete
        winsound.Beep(450, 1500)  # Play a beep sound for 1 second

r = ct.CTk()
r._set_appearance_mode("system")
r.geometry('500x500')
head = ct.CTkLabel(r, text="Welcome to countdown app!", font=('calibri', 30), width=30)
head.pack(pady='15')
r.title("COUNTDOWN APP")

l1 = ct.CTkLabel(r, text="Enter countdown time (seconds): ", font=('calibri', 20))
l1.pack(pady='15')

entry = ct.CTkEntry(r, font=('calibri', 20), placeholder_text="enter in seconds!!", width=175)
entry.pack(pady='15')

def start_countdown_wrapper():
    countdown_time = int(entry.get())  # Get countdown time from entry widget
    start_countdown(countdown_time)

button = ct.CTkButton(r, text="Start Countdown", font=('calibri', 20), hover_color='#b0e0e6', command=start_countdown_wrapper)
button.pack(pady='15')

l2 = ct.CTkLabel(r, text="", font=('calibri', 20))
l2.pack(pady='20')

update_current_time()  # Start updating current time

r.mainloop()
