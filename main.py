# Import local modules
from screen import blank
from functional_objects import label, screen

# Creates objects used in menu.
home = screen(blank)
game_title = label("Darwin Maze Dungeon", label.title)
author = label("Saŭlo Rubusarbaro © 2023", label.regular)

# Set the objects to corresponding screen.
game_title.set_as_text(home, 6, 5)
author.set_as_text(home, 2, 27)

#Print screens.
home.print_screen()
