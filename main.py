import keyboard

from actions import movement
from entities import player
from functions import clearScreen, player_hearts, printScreen

import functionalObjects
import styles

clearScreen()

# Objects definition.
p1 = player()
game = functionalObjects.maze()

p1.set_character(game)
p1_hearts = player_hearts(p1)

print(styles.regular.bold+"VIDA: "+styles.text.end+p1_hearts, styles.regular.bold+"Posición: "+styles.text.end+"%s, %s" %(p1.position[0], p1.position[1]))
printScreen(game)

while True :
     key = keyboard.read_event()

     if key.name == "esc" :
          break
     elif key.event_type == keyboard.KEY_DOWN :
          match key.name :
               case "up" :
                    p1.move(game, movement.UP)
                    clearScreen()
                    print(styles.regular.bold+"VIDA: "+styles.text.end+p1_hearts, styles.regular.bold+"Posición: "+styles.text.end+"%s, %s" %(p1.position[0], p1.position[1]))
                    printScreen(game)
               case "down" :
                    p1.move(game, movement.DOWN)
                    clearScreen()
                    print(styles.regular.bold+"VIDA: "+styles.text.end+p1_hearts, styles.regular.bold+"Posición: "+styles.text.end+"%s, %s" %(p1.position[0], p1.position[1]))
                    printScreen(game)
               case "left" :
                    p1.move(game, movement.LEFT)
                    clearScreen()
                    print(styles.regular.bold+"VIDA: "+styles.text.end+p1_hearts, styles.regular.bold+"Posición: "+styles.text.end+"%s, %s" %(p1.position[0], p1.position[1]))
                    printScreen(game)
               case "right" :
                    p1.move(game, movement.RIGHT)
                    clearScreen()
                    print(styles.regular.bold+"VIDA: "+styles.text.end+p1_hearts, styles.regular.bold+"Posición: "+styles.text.end+"%s, %s" %(p1.position[0], p1.position[1]))
                    printScreen(game)