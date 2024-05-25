from tkinter import *
import datetime
import pygame
import threading


def set_alarm():
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarm_triggered = False

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == set_alarm_time and not alarm_triggered:
            alarm_message()
            alarm_triggered = True
        elif current_time != set_alarm_time:
            alarm_triggered = False


def alarm_message():
    print("Time to Wake up")
    # Initialize pygame mixer
    pygame.mixer.init()
    # Load and play the sound file
    pygame.mixer.music.load("sound.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


# Create the main application window
root = Tk()
root.geometry("400x200")
root.title("Alarm Clock")

# Add a title label
Label(root, text="Alarm Clock", font=("Helvetica", 20, "bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica", 15, "bold")).pack()

# Create a frame for the time setting options
frame = Frame(root)
frame.pack()

# Create dropdown menus for hours, minutes, and seconds
hour = StringVar(root)
hours = [str(i).zfill(2) for i in range(25)]
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = [str(i).zfill(2) for i in range(61)]
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = [str(i).zfill(2) for i in range(61)]
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)


# Function to start the alarm thread
def set_alarm_thread():
    t = threading.Thread(target=set_alarm)
    t.daemon = True
    t.start()


# Add a button to set the alarm
Button(root, text="Set Alarm", font=("Helvetica", 15), command=set_alarm_thread).pack(
    pady=20
)

# Run the main event loop
root.mainloop()
