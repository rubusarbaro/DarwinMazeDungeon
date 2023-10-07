from entities import player
from functional_objects import screen
from screen import maze

game_screen = screen(maze)
p1 = player()

p1.set_in_screen(game_screen)
game_screen.print_screen()