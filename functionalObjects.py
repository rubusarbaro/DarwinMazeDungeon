from screen import maze as maze_layout

class screen(object) :
    def __init__(self) :
        self.layout = []
    
    def print_screen(self) :
        for line in self.layout :
            row = ""
            for item in line :
                row = row + item
            print(row)

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