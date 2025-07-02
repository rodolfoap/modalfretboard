import sys
from colorama import init, Fore, Style

init()
string_color=Fore.BLUE+Style.NORMAL

def print_fret(text, width, fillchar='-', endchar='|', highlight=True):
	if width <= len(text):
		sys.stderr.write(text + '\n')
	else:
		total_padding=width-len(text)
		left_padding=total_padding//2
		right_padding=total_padding-left_padding
		chord_color=Fore.RED+Style.BRIGHT if highlight else string_color
		print(string_color+fillchar*left_padding, end='', flush=True)
		print(chord_color+text, end='', flush=True)
		print(string_color+fillchar*right_padding, end='', flush=True)
		print(string_color+endchar, end='', flush=True)

def print_empty_fret(width, fillchar='-', endchar='|'):
	print(string_color+fillchar*width+endchar, flush=True, end='')
	
def print_reset():
	print(Style.RESET_ALL)