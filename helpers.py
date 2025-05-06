import os

from termcolor import cprint

def clear_view():
    command = 'clear'
    if os.name == 'nt':
        command = 'cls'
    
    os.system(command)

def display_main_menu():
    cprint('My automobiles', 'red', attrs=['bold', 'blink'])
    cprint('1- Full automobiles List', 'blue')
    cprint('2- Add new automobile', 'blue')
    cprint('3- Show specific automobile', 'blue')
    cprint('4- Change automobile', 'blue')
    cprint('5- Eliminate automobile', 'blue')
    cprint('6- Exit', 'red', attrs=['bold', 'blink'])