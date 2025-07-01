#!/bin/env python3
notnames = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
fbsize=22
def fret(note):
	return note.center(6, '-')+'|'

def string(offset):
	for i, x in enumerate(range(offset, offset+fbsize+1)):
		width=3 if i==0 else 6
		print((notnames[x%12]).center(width, '-')+'|', end='')
		#print(fret(, end='')
	print()

def fretboard(scale_intervals):
	# Index line (0, 1, 2, ... 22)
	for x in range(0, fbsize+1):
		width=3 if x==0 else 7
		print(str(x).center(width, ' '), end='')
	print()
	string(4)
	string(11)
	string(7)
	string(2)
	string(9)
	string(4)

c_maj = [0, 2, 4, 5, 7, 9, 11]
fretboard(c_maj)
