# Import local modules.
from functional_objects import button, label, pointer, screen
from functional_objects import list_screens
from screen import blank

# Initialize objects.
main_screen = screen(blank)
screen_title = label("Choose a player", label.title)

# Set objects in screen.
screen_title.set_in_screen(main_screen, 8, 5)

#Print screens.
main_screen.print_screen()
