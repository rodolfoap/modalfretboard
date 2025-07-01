#!/bin/env python3
notnames = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
fbsize=22

def string(offset, scale):
	for i, x in enumerate(range(offset, offset+fbsize+1)):
		x%=12
		width=3 if i==0 else 6
		note_in_scale=notnames[x] if x in scale else '='
		print((note_in_scale).center(width, '-')+'|', end='')
	print()

def fretboard(scale):
	# Index line (0, 1, 2, ... 22)
	print()
	for x in range(0, fbsize+1):
		width=3 if x==0 else 7
		print(str(x).center(width, ' '), end='')
	print()
	string(4, scale)
	string(11, scale)
	string(7, scale)
	string(2, scale)
	string(9, scale)
	string(4, scale)
	print()

c_maj = [0, 2, 4, 5, 7, 9, 11]
fretboard(c_maj)
