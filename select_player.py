# Import local modules.
from functional_objects import button, label, pointer, screen, textbox
from functional_objects import list_screens
from screen import blank

# Initialize objects.
main_screen = screen(blank)
screen_title_label = label("Seleccione su personaje", label.title)
player_name_label = label("Nombre:", label.regular)
player_kind_label = label("Especie:", label.regular)
continue_button = button("Continuar", button.spaced, exit)
back_button = button("Salir", button.spaced, exit)
player_name_input = textbox(20)

# Set objects in screen.
screen_title_label.set_in_screen(main_screen, 4, 5)
player_name_label.set_in_screen(main_screen, 4, 10)
player_kind_label.set_in_screen(main_screen, 4, 15)
continue_button.set_in_screen(main_screen, 11, 20)
back_button.set_in_screen(main_screen, 13, 23)
player_name_input.set_in_screen(player_name_label)

#Print screens.
main_screen.print_screen()
player_name_input.write_in()
