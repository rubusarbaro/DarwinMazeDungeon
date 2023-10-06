# Imports modules
import keyboard

# Imports local modules.
from functions import clear_screen
from styles import backgroung, text

# Created object lists.
list_buttons = []
list_labels = []
list_pointers = []
list_screens = []


class screen :

    """
    Initialize an object of "screen" class. A layout in a list format has to be provided.
    """

    def __init__(self, layout: list) :

        # Appends the created object to the list.
        list_screens.append(self)

        self.layout = layout
        self.width = len(self.layout[0])
        self.height = len(self.layout)
        self.wall_coordinates = self.get_layout_wall_coordinates()
        self.objects_in_screen = []

    def get_layout_wall_coordinates(self) :

        """
        For macOS, get the coordinates in the layout where a "⬜" is placed.
        This method is intended to be used inside the class, in the __init__ method, but it could be used outside too.
        """

        # A list where tupples of coordionates are stored.
        wall_coordinates = []

        # Height and Width values are defined in __init__ method. They represent the lenght of the layout.
        # It searches for the rows and columns containing a "⬜", then it stores them in a tuple as coordinates and appends it to the list.
        for y in range (0, self.height) :
            for x in range (0, self.width) :
                if self.layout[y][x] == "⬜" :
                    wall_coordinates.append((y, x))
        
        return wall_coordinates

    def print_screen(self) :

        """
        Print the layout in the "screen" class object.
        """

        # Cleans the last screen printed.    
        clear_screen()

        # First, it iterates every sublist in the list "layout". Then, it iterates every item in the sublist.
        # It concatenates every item in the sublist to create a row. It prints the row.
        for line in self.layout :
            row = ""
            for item in line :
                row = row + item
            print(row)


class label :

    """
    Initialize an object of "label" class. The text containing the label has to be provided as string.
    The available styles are "regular" and "title".
    """

    def __init__(self, text: str, style) :

        # Appends the created object to the list.
        list_labels.append(self)

        self.text = text
        self.related_screen = None
        self.style = style

    def regular(self) :
        """
        Text without format, as it was initialized.
        It returns the text in a list of two letters per item.
        """

        # Gets the lenght of the text and creates a list where every pair of letter are stored.
        text_len = len(self.text)
        text_as_list = []

        # It iterates a range from 0 to the half of the text length.
        # It uses the half, because it's storing all the letter by pair, not single.
        for i in range(0, text_len//2 ) :
            a = i * 2
            b = a + 1

            string = self.text[a] + self.text[b]
            text_as_list.append(string)

        # It determines if a text lenght is pair or not. If not, it concatenates the last letter to a blank space
        # and append them to the list.
        if text_len//2 != text_len/2 :
            string = self.text[text_len-1] + " "
            text_as_list.append(string)

        return text_as_list
    
    def title(self) :
        """
        Text in title style (uppercase and double space).
        It returns the text in a list of one letter and one space per item.
        """

        # Gets the lenght of the text and creates a list where every pair of letter are stored.
        text_len = len(self.text)
        text_as_list = []

        # It iterates a range from 0 to the half of the text length.
        # It uses the half, because it's storing all the letter by pair, not single.
        for i in range(0, text_len) :
           string = self.text[i] + " "
           text_as_list.append(string.upper())

        return text_as_list

    def set_in_screen(self, screen: object, position_x: int, position_y: int) :

        """
        It adds the text (label) to the assigned screen.
        The target screen, and the position (x and y) of the label has to be provided.
        "screen" is object type. "position_x" and "position_y" are integer type.
        """

        # Assigns the declared screen as related_screen to the object
        self.related_screen = screen
        # Defines the "text_as_list" values according to "label.regular" or "label.title"
        text_as_list = self.style(self)

        # Substitutes every item in the list in the target position.
        for i in range(0, len(text_as_list)) :
            screen.layout[position_y][position_x + i] = text_as_list[i]

        # Adds the current label to a list in the screen, to keep a track of the assigned objects.
        screen.objects_in_screen.append(self)


class button :

    """
    Initialize an object of "button" class. The text containing the label has to be provided as string.
    The available styles are "regular" and "spaced".
    """

    def __init__(self, text: str, style) :

        # Appends the created object to the list.
        list_buttons.append(self)

        self.text = text
        self.related_screen = None
        self.style = style
        self.text_as_list = self.style(self)
        
        self.position_x = 0
        self.position_y = 0

    def regular(self) :
        """
        Text without format, as it was initialized.
        It returns the text in a list of two letters per item.
        """

        # Gets the lenght of the text and creates a list where every pair of letter are stored.
        text_len = len(self.text)
        text_as_list = []

        # It iterates a range from 0 to the half of the text length.
        # It uses the half, because it's storing all the letter by pair, not single.
        for i in range(0, text_len//2 ) :
            a = i * 2
            b = a + 1

            string = self.text[a] + self.text[b]
            text_as_list.append(string)

        # It determines if a text lenght is pair or not. If not, it concatenates the last letter to a blank space
        # and append them to the list.
        if text_len//2 != text_len/2 :
            string = self.text[text_len-1] + " "
            text_as_list.append(string)

        return text_as_list
    
    def spaced(self) :
        """
        Text with double space.
        It returns the text in a list of one letter and one space per item.
        """

        # Gets the lenght of the text and creates a list where every pair of letter are stored.
        text_len = len(self.text)
        text_as_list = []

        # It iterates a range from 0 to the half of the text length.
        # It uses the half, because it's storing all the letter by pair, not single.
        for i in range(0, text_len) :
           string = self.text[i] + " "
           text_as_list.append(string)

        return text_as_list

    def set_in_screen(self, screen: object, position_x: int, position_y: int) :
        """
        It adds the button to the assigned screen.
        The target screen, and the position (x and y) of the button has to be provided.
        "screen" is object type. "position_x" and "position_y" are integer type.
        """

        self.position_x = position_x
        self.position_y = position_y

        # Assigns the declared screen as related_screen to the object
        self.related_screen = screen

        # Substitutes every item in the list in the target position.
        for i in range(0, len(self.text_as_list)) :
            screen.layout[self.position_y][self.position_x + i] = self.text_as_list[i]

        # Adds the current label to a list in the screen, to keep a track of the assigned objects.
        screen.objects_in_screen.append(self)

    def select(self) :
        """
        Underlines text in button when is selected by a pointer.
        """

        counter = 0
        # Iterates every item in the list, then it changes its format accorfing to "styles" module.
        for letter in self.text_as_list :
            letter = backgroung.classic + letter + text.end
            self.related_screen.layout[self.position_y][self.position_x + counter] = letter
            counter = counter + 1

    def unselect(self) :
        """
        Returns the text to the original format.
        """

        counter = 0
        # Iterates every item in the list, then it changes its format accorfing to "styles" module.
        for letter in self.text_as_list :
            self.related_screen.layout[self.position_y][self.position_x + counter] = letter
            counter = counter + 1


class pointer :
    """
    Initialize an object of "pointer" class.
    """

    def __init__(self) :
        # Appends the created object to the list.
        list_pointers.append(self)
        
        self.icon = "->"
        self.related_screen = None
        self.related_button = None

    def set_in_screen(self, screen: object, default_button: object) :
        """
        It adds the button to the assigned screen.
        """
        self.related_screen = screen
        self.related_button = default_button

        self.select_button(self.related_button)
        screen.objects_in_screen.append(self)

    def clear(self) :
        """
        It erase the pointer from the screen without unlinking it.
        """

        position_x = self.related_button.position_x - 2
        position_y = self.related_button.position_y

        self.related_screen.layout[position_y][position_x] = "  "
    
    def select_button(self, button: object) :
        """
        It sets the pointer to a button.
        A button has to be provided.
        """

        # Set the position variables for the pointer.
        position_x = button.position_x - 2
        position_y = button.position_y

        #Set the pointer in the screen.
        self.related_screen.layout[position_y][position_x] = self.icon

        # Change the button format with "select" method.
        button.select()

    def move_to_next(self) :
        """
        Move the position of the button to the next.
        """

        layout_height = len(self.related_screen.layout[0])

        in_screen_buttons = {}
        for button in list_buttons :
            if button.related_screen == self.related_screen :
                in_screen_buttons[button.position_y] = button

        while True:
            key = keyboard.read_event()
        
            if key.name == "esc" :
                exit()
            if key.name == "enter" :
                print("Botón presionado")
                exit()

            match key.name :
                case "up" | "left" :
                    self.related_button.unselect()
                    self.clear()

                    relative_position_y =self.related_button.position_y - 1
                    for i in range(0, relative_position_y) :
                        if relative_position_y - i in in_screen_buttons :
                            self.related_button = in_screen_buttons[relative_position_y - i]
                            new_position_x = self.related_button.position_x - 2
                            new_position_y = self.related_button.position_y
                        
                            self.select_button(self.related_button)
                            self.related_screen.layout[new_position_y][new_position_x] = self.icon
                case "down" | "right" :
                    self.related_button.unselect()
                    self.clear()

                    relative_position_y = self.related_button.position_y + 1
                    iterative = layout_height - self.related_button.position_y
                    for i in range(0, iterative) :
                        if relative_position_y + i in in_screen_buttons :
                            self.related_button = in_screen_buttons[relative_position_y + i]
                            new_position_x = self.related_button.position_x - 2
                            new_position_y = self.related_button.position_y
                        
                            self.select_button(self.related_button)
                            self.related_screen.layout[new_position_y][new_position_x] = self.icon
            
            self.related_screen.print_screen()
