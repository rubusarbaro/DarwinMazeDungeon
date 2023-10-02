from functions import clearScreen
from screen import maze as maze_layout
from styles import backgroung, text

#List of all the objects created.
list_screens = []
list_menus = []
list_games = []
list_pointers = []
list_buttons = []

class screen(object) :
    def __init__(self) :
        list_screens.append(self)
        self.layout = []
    
    def print_screen(self) :
        clearScreen()
        for line in self.layout :
            row = ""
            for item in line :
                row = row + item
            print(row)

class menu(screen) :
    def __init__(self, screen: list):
        list_menus.append(self)
        self.layout = screen

class game(screen) :
    def __init__(self) :
        list_games.append(self)
        self.layout = maze_layout
        self.wall_coordinates = self.get_wall_coordinates()

    def get_wall_coordinates(self) :
        layout_height = len(self.layout)
        layout_width = len(self.layout[0])

        wall_coordinates = []
        for y in range (0, layout_height) :
            for x in range (0, layout_width) :
                if self.layout[y][x] == "⬜" :
                    wall_coordinates.append([y, x])
        
        return wall_coordinates

class pointer :
    def __init__(self) :
        list_pointers.append(self)
        self.icon = "->"
        self.position_x = 0
        self.position_y = 0

    def set_default_button(self, screen: object, button: object) :
        self.position_x = button.init_position_x -2
        self.position_y = button.init_position_y
        screen.layout[self.position_y][self.position_x] = self.icon

    def select_button(self) :
        for any in list_buttons :
            print(any.text)
            if any.is_selected() :
                for letter in any.text_as_list :
                    letter = backgroung.classic + letter + text.end
        #SIN TERMINAR


    """
    def set_position(self, screen: object) :
        self.init_position_x = screen.main_button[1] - 2
        self.init_position_y = screen.main_button[0]

        screen.layout[self.init_position_y][self.init_position_x] = self.icon
    """

class button :
    def __init__(self, text: str, ) :
        list_buttons.append(self)
        self.text = text
        self.text_len = len(self.text)
        self.text_as_list = []

        for i in range(0, self.text_len) :
            self.text_as_list.append(" %s" %(self.text[i]))

        self.init_position_x = 0
        self.init_position_y = 0

    def set_position(self, screen: object, position_x: int, position_y: int) :
        for i in range(0, self.text_len) :
            screen.layout[position_y][position_x+i] = self.text_as_list[i]
        self.init_position_x = position_x
        self.init_position_y = position_y
    
    def is_selected(self) :
        for any in list_pointers :
            if any.position_y == self.init_position_y and any.position_x == self.init_position_x - 2 :
                return True
        return False