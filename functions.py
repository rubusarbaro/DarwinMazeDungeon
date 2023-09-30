import os

def printScreen(screen) :
     for line in screen[0] :
          row = ""
          for item in line :
               row = row + item
          print(row)

def clearScreen() :
    if os.name == "posix" :
        os.system("clear")
    elif os.name == "nt" :
         os.system("CLS")
    else :
        print("Function not compatible with the current os.")