class player :
    def __init__(self) :
        self.icon = "🧙🏼‍♂️"
        self.init_position = (19, 16)
        self.position = [self.init_position[0], self.init_position[1]]
        self.life = 3

    def set_character(self, screen) :
        screen[0][self.position[0]][self.position[1]] = self.icon
    
    def move(self, screen, movement) :
        posible_position = [self.position[0] + movement[0], self.position[1] + movement[1]]

        if posible_position in screen[1] :
            return
        else: 
            screen[0][self.position[0]][self.position[1]] = "⬛️"
            self.position[0] = self.position[0] + movement[0]
            self.position[1] = self.position[1] + movement[1]
            self.set_character(screen)