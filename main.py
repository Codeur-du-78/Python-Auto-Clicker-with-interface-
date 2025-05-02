# Python-Auto-Clicker-with-interface-
#This is a Python autoclicker that has an interface and allows you to choose the number of CPS you want, you can edit the code to make changes, or customize the code.
import time
code :



import threading
import tkinter as tk
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

# Key to toggle the auto clicker
TOGGLE_KEY = KeyCode(char="t")

clicking = False
mouse = Controller()
cps = 10  # Initial clicks per second

def clicker():
    global cps
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(1 / cps)  # Wait based on current CPS
        else:
            time.sleep(0.01)  # Short delay to reduce CPU usage

def toggle_event(Key):
    if Key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

def set_cps(new_cps):
    global cps
    cps = int(new_cps)  # Update CPS with user input

# Create the GUI
root = tk.Tk()
root.title("Auto Clicker")

# Label to show current CPS
cps_label = tk.Label(root, text=f"Current CPS: {cps}", font=("Arial", 14))
cps_label.pack(pady=10)

# Input field to set the CPS
cps_entry = tk.Entry(root, font=("Arial", 14))
cps_entry.insert(0, str(cps))  # Default CPS value
cps_entry.pack(pady=10)

# Button to apply the new CPS
apply_button = tk.Button(root, text="Apply", font=("Arial", 14), command=lambda: set_cps(cps_entry.get()))
apply_button.pack(pady=10)

# Function to close the GUI and stop clicking
def close_app():
    global clicking
    clicking = False
    root.quit()

# Button to stop the program
close_button = tk.Button(root, text="Stop", font=("Arial", 14), command=close_app)
close_button.pack(pady=10)

# Start the clicker thread
click_thread = threading.Thread(target=clicker)
click_thread.start()

# Start the keyboard listener
with Listener(on_press=toggle_event) as listener:
    # Start the GUI main loop
    root.mainloop()
    listener.join()
