class character(object):
    """
    Initialize an object of "character" class.
    The main type of characters are: "player" and "npc".
    """

    def __init__(self) :
        self.icon = None
        self.init_position_x = None
        self.init_position_y = None

class player :
    """
    Initialize an object of "player" class. A layout in a list format has to be provided.
    """

    def __init__(self) :
        self.icon = "🧙🏼‍♂️"
        self.init_position_x = 16
        self.init_position_y = 19

    def set_in_screen(self, screen: object) :
        screen.layout[self.init_position_y][self.init_position_x] = self.icon