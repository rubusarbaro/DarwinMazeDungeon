from screen import blank
from functional_objects import label, screen

home = screen(blank)
author = label("Saŭlo Rubusarbaro © 2023")
author.set_as_text(home, 2, 27)
home.print_screen()