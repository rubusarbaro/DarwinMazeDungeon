import os

def clear_screen() :

    """
    Clear all text in the terminal.
    """

    # If system is macOS or Linux, it will use "clear" command.
    if os.name == "posix" :
        os.system("clear")
    # Else, if it's Windows, it will use "CLS".
    elif os.name == "nt" :
         os.system("CLS")
    # If a system doesn't match any of this conditions, it will display an error.
    else :
        print("Function not compatible with the current os.")