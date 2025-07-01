from print_center import print_center

chromatic = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
modes={	'ionian': 0, 'dorian': 2, 'phrygian': 4, 'lydian': 5, 'mixolydian': 7, 'aeolian': 9, 'locrian': 11 }
natscale = [0, 2, 4, 5, 7, 9, 11]

fbsize=22
fillchar='-'

def string(offset, scale):
	# (fret, chromatic_note): (0, 4->E), (1, 5->F), (2, 6->F#) ...
	for fret, chromatic_note in enumerate(range(offset, offset+fbsize+1)):
		chromatic_note%=12 # rotate down in case it exceeds 12
		width=3 if fret==0 else 6 # just for printing

		# If the chromatic note corresponding to this fret is in the scale
		if chromatic[chromatic_note] in scale:
			print_center(chromatic[chromatic_note], width, fillchar, '|')
		else:
			print('-'*width+'|', flush=True, end='')
	print()

def fretboard(scale):
	# Index line (0, 1, 2, ... 22)
	print()
	print(scale)
	for x in range(0, fbsize+1): print(str(x).center(3 if x==0 else 7, ' '), end='')
	print()
	string(4, scale)
	string(11, scale)
	string(7, scale)
	string(2, scale)
	string(9, scale)
	string(4, scale)
