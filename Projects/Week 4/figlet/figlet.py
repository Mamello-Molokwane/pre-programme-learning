import sys
import random
import pyfiglet

def command_line():
    if len(sys.argv) > 1:
        if sys.argv[1] == '-f' or sys.argv[1] == '--font':
            try:
                if pyfiglet.figlet_format('text', font=sys.argv[2]) == pyfiglet.FontNotFound:
                    raise pyfiglet.FontNotFound
                user_input = input('Input: ')
                font = pyfiglet.figlet_format(user_input, font=sys.argv[2])
            except pyfiglet.FontNotFound:
                sys.exit('Invalid usage')
            print(font)
        else:
            sys.exit('Invalid usage')
    elif len(sys.argv) < 2:
        user_input = input('Input: ')
        font = pyfiglet.figlet_format(user_input)
        print(font)

command_line()
