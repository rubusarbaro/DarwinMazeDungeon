import keyboard

from actions import movement
from entities import player
from functions import clearScreen, printScreen
from screen import screen

clearScreen()

p1 = player()

p1.set_character(screen)
printScreen(screen)

while True :
     key = keyboard.read_event()

     if key.name == "esc" :
          break
     elif key.event_type == keyboard.KEY_DOWN :
          match key.name :
               case "up" :
                    p1.move(screen, movement.UP)
                    clearScreen()
                    printScreen(screen)
               case "down" :
                    p1.move(screen, movement.DOWN)
                    clearScreen()
                    printScreen(screen)
               case "left" :
                    p1.move(screen, movement.LEFT)
                    clearScreen()
                    printScreen(screen)
               case "right" :
                    p1.move(screen, movement.RIGHT)
                    clearScreen()
                    printScreen(screen)