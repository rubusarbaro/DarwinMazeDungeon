from functions import clearScreen
from screen import maze as maze_layout

class screen(object) :
    def __init__(self) :
        self.layout = []
    
    def print_screen(self) :
        clearScreen()
        for line in self.layout :
            row = ""
            for item in line :
                row = row + item
            print(row)

class menu(screen) :
    def __init__(self, screen: object, main_button_position: tuple):
        self.layout = screen
        self.main_button = main_button_position

class game(screen) :
    def __init__(self) :
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
        self.icon = "->"
        self.init_position_x = 0
        self.init_position_y = 0

    def set_position(self, screen: object) :
        self.init_position_x = screen.main_button[1] - 2
        self.init_position_y = screen.main_button[0]

        screen.layout[self.init_position_y][self.init_position_x] = self.icon