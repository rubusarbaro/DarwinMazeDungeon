import os

def printScreen(screen) :
     for line in screen.layout :
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

def player_hearts(player) :
     hearts = ""
     for i in range(0, player.life) :
          hearts = hearts + "❤️ "
     return hearts