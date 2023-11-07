from pynput import keyboard


def on_press(key) :
    try :
        return False
    except AttributeError :
        return False

with keyboard.Listener(
    on_press=on_press
) as listener :
    listener.join()