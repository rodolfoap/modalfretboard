#!/bin/env python3
from colorama import init, Fore, Style

init()
#print(Fore.GREEN + Back.BLACK + Style.BRIGHT + 'some text')
print(Fore.BLUE + '---', end='')
print(Fore.GREEN + 'C#', end='')
print(Fore.BLUE + '---', end='')
print(Fore.BLUE + '---', end='')
print(Fore.BLUE+Style.BRIGHT + 'C#', end='')
print(Fore.BLUE + '---', end='')
print(Style.RESET_ALL)
print('back to normal now')

