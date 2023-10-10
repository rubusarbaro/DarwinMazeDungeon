# Import modules
from copy import deepcopy
import keyboard

# Import local modules.
from functions import clear_screen
from styles import bold, background, text

# Created object lists.
list_buttons = []
list_input_box = []
list_labels = []
list_pointers = []
list_screens = []


class screen :

    """
    Initialize an object of "screen" class. A layout in a list format has to be provided.
    """

    def __init__(self, layout: list) :

        # Append the created object to the list.
        list_screens.append(self)

        self.layout = deepcopy(layout) # Deepcopy used to avoid that all changes in the layout affects the original.
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

        # Clean the last screen printed.    
        clear_screen()

        # First, it iterates every sublist in the list "layout". Then, it iterates every item in the sublist.
        # It concatenates every item in the sublist to create a row. It prints the row.
        for line in self.layout :
            row = ""
            for item in line :
                row += item
            print(row)


class label :

    """
    Initialize an object of "label" class. The text containing the label has to be provided as string.
    The available styles are "regular" and "title".
    """

    def __init__(self, text: str, style) :

        # Append the created object to the list.
        list_labels.append(self)

        self.text = text
        self.related_screen = None
        self.style = style

        self.position_x = 0
        self.position_y = 0

    def regular(self) :
        """
        Text without format, as it was initialized.
        It returns the text in a list of two letters per item.
        """

        # Get the lenght of the text and creates a list where every pair of letter are stored.
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

        # Get the lenght of the text and creates a list where every pair of letter are stored.
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

        # Store the postion atributes in the object's.
        self.position_x = position_x
        self.position_y = position_y

        # Assigns the declared screen as related_screen to the object
        self.related_screen = screen
        # Defines the "text_as_list" values according to "label.regular" or "label.title"
        text_as_list = self.style(self)

        # Substitutes every item in the list in the target position.
        for i in range(0, len(text_as_list)) :
            screen.layout[self.position_y][self.position_x + i] = text_as_list[i]

        # Adds the current label to a list in the screen, to keep a track of the assigned objects.
        screen.objects_in_screen.append(self)


class button :

    """
    Initialize an object of "button" class. The text containing the label has to be provided as string.
    The available styles are "regular" and "spaced".
    """

    def __init__(self, text: str, style, action) :

        # Append the created object to the list.
        list_buttons.append(self)

        self.text = text
        self.related_screen = None
        self.style = style
        self.text_as_list = self.style(self)
        
        self.position_x = 0
        self.position_y = 0

        self.is_selected = False
        self.action = action

    def regular(self) :
        """
        Text without format, as it was initialized.
        It returns the text in a list of two letters per item.
        """

        # Get the lenght of the text and creates a list where every pair of letter are stored.
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

        # Get the lenght of the text and creates a list where every pair of letter are stored.
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

        # Assign the declared screen as related_screen to the object
        self.related_screen = screen

        # Substitute every item in the list in the target position.
        for i in range(0, len(self.text_as_list)) :
            screen.layout[self.position_y][self.position_x + i] = self.text_as_list[i]

        # Add the current label to a list in the screen, to keep a track of the assigned objects.
        screen.objects_in_screen.append(self)

    def select(self) :
        """
        Underlines text in button when is selected by a pointer.
        """

        counter = 0
        # Iterate every item in the list, then it changes its format accorfing to "styles" module.
        for letter in self.text_as_list :
            letter = background.classic + letter + text.end
            self.related_screen.layout[self.position_y][self.position_x + counter] = letter
            counter += 1
        
        self.is_selected = True

    def unselect(self) :
        """
        Returns the text to the original format.
        """

        counter = 0
        # Iterate every item in the list, then it changes its format accorfing to "styles" module.
        for letter in self.text_as_list :
            self.related_screen.layout[self.position_y][self.position_x + counter] = letter
            counter += 1

        self.is_selected = False


class pointer :
    """
    Initialize an object of "pointer" class.
    """

    def __init__(self) :
        # Append the created object to the list.
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

        # Calculate the height of the layout to determine the possible quantity of buttons in a screen.
        layout_height = len(self.related_screen.layout[0])

        # Create a dictionary of all the buttons in the screen. The key is button.position_y
        in_screen_buttons = {}
        for button in list_buttons :
            if button.related_screen == self.related_screen :
                in_screen_buttons[button.position_y] = button

        # It iterates until one of two conditions is met: "esc" key pressed or "enter" key pressed when selected a button.
        while True:
            key = keyboard.read_event()
        
            # If "esc" key is pressed, it finish the program.
            if key.name == "esc" :
                exit()

            # If "enter" key us pressed, it executes the action in the button.
            # It determines what button is selected based on the screen and position_y of the button and the pointer.
            if key.name == "enter" :
                for button in list_buttons :
                    if button.related_screen == self.related_screen and button.position_y == self.related_button.position_y :
                        button.action()
                        return

            # If a key is pressed, it compares the following conditions:
            if key.event_type == keyboard.KEY_DOWN :
                match key.name :

                    # If key name is "up" or "left", it searches the buttons above the selected one.
                    # This only works in macOS and probably in Linux too. It's necessary find a solution for Windows.
                    case "up" | "left" :

                        # It sets a relative position_y to start to find the possible buttons above the current.
                        # It iterates a range from 0 to reltive_position_y. For each iteration, it searches in the dictionary if there's
                        # a key with the position_y (for example: 9, 8, 7, 6, 5...) When it finds it, it select the first.
                        relative_position_y = self.related_button.position_y - 1
                        for i in range(0, relative_position_y) :
                            if relative_position_y - i in in_screen_buttons :
                                # First, it unselect the current button and erase the pointer from its current position.
                                self.related_button.unselect()
                                self.clear()

                                # It changes the current related button (of the pointer) by the new, the it changes its position
                                # to the button's one.
                                self.related_button = in_screen_buttons[relative_position_y - i]
                                new_position_x = self.related_button.position_x - 2
                                new_position_y = self.related_button.position_y
                            
                                # It selects the new button and set the new position for the pointer.
                                self.select_button(self.related_button)
                                self.related_screen.layout[new_position_y][new_position_x] = self.icon

                    # If key name is "down" or "right", it searches the buttons below the selected one.
                    # This only works in macOS and probably in Linux too. It's necessary find a solution for Windows.     
                    case "down" | "right" :

                        # It sets a relative position_y to start to find the possible buttons below the current.
                        # It iterates a range from 0 to reltive_position_y. For each iteration, it searches in the dictionary if there's
                        # a key with the position_y (for example: 10, 11, 12, 13, 14...) When it finds it, it select the first.
                        relative_position_y = self.related_button.position_y + 1
                        iterative = layout_height - self.related_button.position_y
                        for i in range(0, iterative) :
                            if relative_position_y + i in in_screen_buttons :
                                # First, it unselect the current button and erase the pointer from its current position.
                                self.related_button.unselect()
                                self.clear()
                                
                                # It changes the current related button (of the pointer) by the new, the it changes its position
                                # to the button's one.
                                self.related_button = in_screen_buttons[relative_position_y + i]
                                new_position_x = self.related_button.position_x - 2
                                new_position_y = self.related_button.position_y

                                # It selects the new button and set the new position for the pointer.
                                self.select_button(self.related_button)
                                self.related_screen.layout[new_position_y][new_position_x] = self.icon
                
                #Finally, it prints the screen with the new positions.
                self.related_screen.print_screen()

class textbox :
    """
    Initialize an object of "input_box" class.
    A size value (character) has to be provided to initializate the object.
    """

    def __init__(self, size: int) :
        list_input_box.append(self)

        self.position_x = 0
        self.position_y = 0
        self.size = size
        self.layout = self.build_layout()
        self.legend = None

        self.related_screen = None
        self.related_label = None

        self.value = ""
    
    def build_layout(self) :
        """
        It builds the textbox accoriding to the length provided when initializated.
        """

        # If the size provided is minor to 1, it sets the value to 1.
        if self.size < 1 :
            self.size = 1

        # Creates a row with the first line of the box. Size is determined by the provided at inizialization.
        line1 = " "
        line1_end = " "
        for i in range(0, self.size) :
            line1 += "_"
        line1 += line1_end

        # Creates a row with the second line of the box. Size is determined by the provided at inizialization.
        line2 = "⎢"
        line2_end = "⎪"
        for i in range(0, self.size) :
            line2 += " "
        line2 += line2_end

        # Creates a row with the third line of the box. Size is determined by the provided at inizialization.
        line3 = " "
        line3_end = " "
        for i in range(0, self.size) :
            line3 += "⎺"
        line3 += line3_end

        lines = [line1, line2, line3]

        box = []
        absolute_textbox_len = self.size + 2
        for line in lines :
            row = []
            for i in range(0, absolute_textbox_len // 2) :
                a = i * 2
                b = a + 1

                string = line[a] + line[b]
                row.append(string)

            if absolute_textbox_len // 2 != absolute_textbox_len / 2 :
                string = line[absolute_textbox_len - 1] + " "
                row.append(string)

            box.append(row)             
        
        return box

    def set_in_screen(self, label: object) :
        """
        It sets the textbox in the screen according to the postion of the label in the screen.
        A label has to be provided. 
        """

        self.related_label = label
        self.related_screen = label.related_screen

        label_len = len(label.text)
        if label_len //2 != label_len / 2 :
            label_len = label_len + 1
        label_relative_len = label_len / 2
            
        self.position_x = label.position_x + int(label_relative_len) + 1
        self.position_y = label.position_y

        try :
            row_counter = -1
            for row in self.layout :
                for i in range(0, len(row)) :
                    self.related_screen.layout[self.position_y + row_counter][self.position_x + i] = row[i]
                row_counter += 1
        except :
            print(bold.red+"Error: "+text.end+"The size of the textbox is larger than the screen layout.")
            exit()

    def set_legend(self, message: str) :
        """
        Set an explanatory legend. It's optional.
        """

        self.legend = message
    
    def write_in(self) :
        """
        It allows user to write in the textbox.
        """

        # If a legend is provided, it will print it below the textbox.
        if self.legend != None :
            legend = label(self.legend)
            legend.set_in_screen(self.related_screen, self.position_x, self.position_y + 2)

        text_in_box = label(None, label.regular)

        while True :
            key = keyboard.read_event()

            if key.event_type == keyboard.KEY_DOWN and key.name is not None :
                if key.name.isalnum() :
                    self.value += key.name
                    text_in_box.set_in_screen(self.related_screen, self.position_x + 1, self.position_y)
                    self.related_screen.print_screen()
                elif key.name == "enter":
                    return
                elif key.name == "delete":
                    pass