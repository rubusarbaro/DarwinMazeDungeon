import keyboard

from actions import movement
from entities import player
from functions import clearScreen, player_hearts, printScreen
from screen import screen

import styles

clearScreen()

p1 = player()

p1.set_character(screen)
p1_hearts = player_hearts(p1)

print(styles.regular.bold+"VIDA: "+styles.text.end+p1_hearts, styles.regular.bold+"Posición: "+styles.text.end+"%s, %s" %(p1.position[0], p1.position[1]))
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
                    print(styles.regular.bold+"VIDA: "+styles.text.end+p1_hearts, styles.regular.bold+"Posición: "+styles.text.end+"%s, %s" %(p1.position[0], p1.position[1]))
                    printScreen(screen)
               case "down" :
                    p1.move(screen, movement.DOWN)
                    clearScreen()
                    print(styles.regular.bold+"VIDA: "+styles.text.end+p1_hearts, styles.regular.bold+"Posición: "+styles.text.end+"%s, %s" %(p1.position[0], p1.position[1]))
                    printScreen(screen)
               case "left" :
                    p1.move(screen, movement.LEFT)
                    clearScreen()
                    print(styles.regular.bold+"VIDA: "+styles.text.end+p1_hearts, styles.regular.bold+"Posición: "+styles.text.end+"%s, %s" %(p1.position[0], p1.position[1]))
                    printScreen(screen)
               case "right" :
                    p1.move(screen, movement.RIGHT)
                    clearScreen()
                    print(styles.regular.bold+"VIDA: "+styles.text.end+p1_hearts, styles.regular.bold+"Posición: "+styles.text.end+"%s, %s" %(p1.position[0], p1.position[1]))
                    printScreen(screen)