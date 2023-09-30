from arcade import key

def on_press(keylog) :
    if keylog == key.W :
        print("UP")
    elif keylog == key.S :
        print("DOWN")
    elif keylog == key.A :
        print("LEFT")
    elif keylog == key.D :
        print("RIGHT")