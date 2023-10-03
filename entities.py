class player :
    def __init__(self) :
        self.icon = "🧙🏼‍♂️"
        self.init_position = (19, 16)
        self.position = [self.init_position[0], self.init_position[1]]
        self.life = 3

    def set_character(self, screen: object) :
        screen.layout[self.position[0]][self.position[1]] = self.icon
    
    def move(self, screen: object, movement) :
        possible_position = [self.position[0] + movement[0], self.position[1] + movement[1]]

        if possible_position in screen.wall_coordinates :
            return
        else: 
            screen.layout[self.position[0]][self.position[1]] = "  "
            self.position[0] = possible_position[0]
            self.position[1] = possible_position[1]
            self.set_character(screen)