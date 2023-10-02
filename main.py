import gc
import keyboard

from actions import movement
from entities import player
from functions import clearScreen, player_hearts

import functionalObjects
import screen
import styles

clearScreen()

# Objects definition.
p1 = player()
main_home = functionalObjects.menu(screen.home)
maze = functionalObjects.game()
pointer = functionalObjects.pointer()
button_start = functionalObjects.button("Iniciar")
button_exit = functionalObjects.button("Salir")

button_start.set_position(main_home, 12, 10)
button_exit.set_position(main_home, 13, 14)
pointer.set_default_button(main_home, button_start)
main_home.print_screen()
input("Presiona (enter) para continuar...")
# PENDIENTE TERMINAR DE LA 21 EN ADELANTE.

p1.set_character(maze)
p1_hearts = player_hearts(p1)

print(styles.regular.bold+"VIDA: "+styles.text.end+p1_hearts, styles.regular.bold+"Posición: "+styles.text.end+"%s, %s" %(p1.position[0], p1.position[1]))
maze.print_screen()

while True :
     key = keyboard.read_event()

     if key.name == "esc" :
          break
     elif key.event_type == keyboard.KEY_DOWN :
          match key.name :
               case "up" :
                    p1.move(maze, movement.UP)
                    print(styles.regular.bold+"VIDA: "+styles.text.end+p1_hearts, styles.regular.bold+"Posición: "+styles.text.end+"%s, %s" %(p1.position[0], p1.position[1]))
                    maze.print_screen()
               case "down" :
                    p1.move(maze, movement.DOWN)
                    print(styles.regular.bold+"VIDA: "+styles.text.end+p1_hearts, styles.regular.bold+"Posición: "+styles.text.end+"%s, %s" %(p1.position[0], p1.position[1]))
                    maze.print_screen()
               case "left" :
                    p1.move(maze, movement.LEFT)
                    print(styles.regular.bold+"VIDA: "+styles.text.end+p1_hearts, styles.regular.bold+"Posición: "+styles.text.end+"%s, %s" %(p1.position[0], p1.position[1]))
                    maze.print_screen()
               case "right" :
                    p1.move(maze, movement.RIGHT)
                    print(styles.regular.bold+"VIDA: "+styles.text.end+p1_hearts, styles.regular.bold+"Posición: "+styles.text.end+"%s, %s" %(p1.position[0], p1.position[1]))
                    maze.print_screen()
