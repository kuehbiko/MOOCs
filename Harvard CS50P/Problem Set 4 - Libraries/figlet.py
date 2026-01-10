# https://cs50.harvard.edu/python/2022/psets/4/figlet/

# import libraries
import sys
from random import choice
from pyfiglet import Figlet

# define global variables
figlet = Figlet()
figlet_fonts = figlet.getFonts() # list of fonts
sys_argvs = ["-f", "--font"] # list of accepted command-line arguments

def figma():
    if len(sys.argv) < 2: # if only 1 argument
        text = input("Input: ") # ask for input only after sys.argv conditions are satisfied
        figlet.setFont(font = choice(figlet_fonts))

    elif (len(sys.argv) ==3) and (sys.argv[1] in sys_argvs) and (sys.argv[2] in figlet_fonts): # if 3 args and all arguments are valid
        text = input("Input: ")
        figlet.setFont(font = sys.argv[2])

    else:
        sys.exit("Invalid usage")

    print(figlet.renderText(text))

figma()
