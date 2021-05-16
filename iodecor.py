#!/usr/bin/env python3

import os



if __name__ == '__main__':
   print("\nExecuted \'" + os.path.basename(__file__) + "\' directly.\n")
else:
   print("\nExecuted \'" + os.path.basename(__file__) + "\' indirectly.\n")



def centertext(text):
   middle = os.get_terminal_size().columns - int(float(len(text))/2) 
   # closely calculates center xposition of where the string would be
           ### TEST ###
        #   print("TEXT: " + text)
        #   print(
        #       "WIDTH: " + str(os.get_terminal_size().columns) + 
        #       "\nTEXT LENGTH: " + str(len(text)) +
        #       "\nTEXT LENGTH HALF: " + str(int(float(len(text))/2)) + 
        #       "\nMIDDLE: " + str(middle)
        #   )
   return text.center(middle)

COLORS = {\
        "black":"\u001b[30;1m",
        "red":"\u001b[31;1m",
        "green":"\u001b[32m",
        "yellow":"\u001b[33;1m",
        "blue":"\u001b[34;1m",
        "magenta":"\u001b[35m",
        "cyan": "\u001b[36m",
        "white":"\u001b[37m",
        "yellow-background":"\u001b[43m",
        "black-background":"\u001b[40m",
        "cyan-background":"\u001b[46;1m",
        "RESET":"\u001b[0m",
}
def colorText(text):
        for color in COLORS:
                text = text.replace("[[" + color + "]]", COLORS[color])
        return text
