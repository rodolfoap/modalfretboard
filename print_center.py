import sys

def print_center(text, width, fillchar='-', endchar='', highlight=True):
	if len(fillchar) != 1: raise ValueError("fillchar must be a single character")
	text_length = len(text)
	if width <= text_length:
		sys.stderr.write(text + '\n')
		return
	total_padding = width - text_length
	left_padding = total_padding // 2
	right_padding = total_padding - left_padding
	channel=sys.stderr if highlight else sys.stdout
	print(fillchar * left_padding, file=sys.stdout, end='', flush=True)
	print(text, file=channel, end='', flush=True)
	print(fillchar * right_padding, file=sys.stdout, end='', flush=True)
	print(endchar, end='', flush=True)
