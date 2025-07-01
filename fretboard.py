from print_center import print_center

chromatic = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
modes={	'ionian': 0, 'dorian': 2, 'phrygian': 4, 'lydian': 5, 'mixolydian': 7, 'aeolian': 9, 'locrian': 11 }
natscale = [0, 2, 4, 5, 7, 9, 11]

fbsize=22
fillchar='-'

def string(offset, scale):
	for i, x in enumerate(range(offset, offset+fbsize+1)):
		x%=12
		width=3 if i==0 else 6
		if x in scale:
			print_center(chromatic[x], width, fillchar, '|')
		else:
			print('-'*width+'|', flush=True, end='')
	print()

def fretboard(scale):
	# Index line (0, 1, 2, ... 22)
	print()
	for x in range(0, fbsize+1): print(str(x).center(3 if x==0 else 7, ' '), end='')
	print()
	string(4, scale)
	string(11, scale)
	string(7, scale)
	string(2, scale)
	string(9, scale)
	string(4, scale)
