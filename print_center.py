#!/bin/env python3
import sys

def print_center(text, width, fillchar='-', endchar=''):
	if len(fillchar) != 1: raise ValueError("fillchar must be a single character")
	text_length = len(text)
	if width <= text_length:
		sys.stderr.write(text + '\n')
		return
	total_padding = width - text_length
	left_padding = total_padding // 2
	right_padding = total_padding - left_padding
	#sys.stdout.write(fillchar * left_padding)
	#sys.stderr.write(text)
	#sys.stdout.write(fillchar * right_padding + '\n')
	print(fillchar * left_padding, file=sys.stdout, end='', flush=True)
	print(text, file=sys.stderr, end='', flush=True)
	print(fillchar * right_padding, file=sys.stdout, end='', flush=True)
	print(endchar, end='', flush=True)

# Example usage
# print_center("hello", 15)
