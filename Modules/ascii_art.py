# from pyfiglet import Figlet
#
#
# f = Figlet(font='standard', colors="magenta")
# print(f.renderText('message'))

import pyfiglet

message = input("What message do you want to print? ")
color = input("What color? ")
COLOR_CODES = {'BLACK': 30, 'RED': 31, 'GREEN': 32, 'YELLOW': 33, 'BLUE': 34, 'MAGENTA': 35, 'CYAN': 36, 'LIGHT_GRAY': 37,
               'DEFAULT': 39, 'DARK_GRAY': 90, 'LIGHT_RED': 91, 'LIGHT_GREEN': 92, 'LIGHT_YELLOW': 93, 'LIGHT_BLUE': 94,
               'LIGHT_MAGENTA': 95, 'LIGHT_CYAN': 96, 'WHITE': 97, 'RESET': 0
               }
if color.upper() not in COLOR_CODES.keys():
    color = "magenta"

f = pyfiglet.print_figlet(message, font="standard", colors=color)
