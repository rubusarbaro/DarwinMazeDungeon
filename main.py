# Import modules
import os

# Check if the system is Windows. If it is, it prints an error and exits.
if os.name == "nt" :
     os.system("COLOR")
     print(styles.bold.red+"Error: "+styles.text.end+"Este programa no es compatible con Windows, solamente con macOS y Linux.")
     exit()

# Import the menu.
import main_menu