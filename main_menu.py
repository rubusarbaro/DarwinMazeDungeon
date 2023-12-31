from functions import select_player
from functional_objects import button, label, pointer, screen
from screen import blank

# Creates objects used in menu.
home_screen = screen(blank)
game_title = label("Darwin Maze Dungeon", label.title)
author_label = label("Saŭlo Rubusarbaro © 2023", label.regular)
start_button = button("Iniciar", button.spaced, select_player)
exit_button = button("Salir", button.spaced, exit)
cursor = pointer()

# Set the objects to corresponding screen.
game_title.set_in_screen(home_screen, 6, 5)
author_label.set_in_screen(home_screen, 2, 27)
start_button.set_in_screen(home_screen, 12, 12)
exit_button.set_in_screen(home_screen, 13, 17)

# Set the pointer in the screen.
cursor.set_in_screen(home_screen, start_button)

#Print screens.
home_screen.print_screen()

cursor.move_to_next()