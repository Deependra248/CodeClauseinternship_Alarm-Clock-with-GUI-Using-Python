import tkinter as tk
import time
import winsound

def set_alarm():
    alarm_time = entry.get()
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            # Play the alarm sound
            winsound.Beep(10000, 10000)  # Beep at 1000 Hz for 1 second
            break

# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Create and configure widgets
label = tk.Label(root, text="Enter alarm time (HH:MM):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(pady=10)

# Start the main loop
root.mainloop()


