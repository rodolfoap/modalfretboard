import sys
from output import print_fret, print_empty_fret, print_reset, print_init

#hromatic = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
chromatic = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
modes={	'ionian': 0, 'dorian': 2, 'phrygian': 4, 'lydian': 5, 'mixolydian': 7, 'aeolian': 9, 'locrian': 11 }
natscale = [0, 2, 4, 5, 7, 9, 11]

fbsize=22

def string(offset, scale, common_tones):
	# (fret, chromatic_note): (0, 4->E), (1, 5->F), (2, 6->F#) ...
	for fret, chromatic_note in enumerate(range(offset, offset+fbsize+1)):
		chromatic_note%=12 # rotate down in case it exceeds 12
		width=3 if fret==0 else 6 # just for printing

		# If the chromatic note corresponding to this fret is in the scale
		note=chromatic[chromatic_note]
		is_common=True if note in common_tones else False
		if note in scale:
			print_fret(note, width, highlight=is_common)
		else:
			print_empty_fret(width)
	print_reset()

def fretboard(scale_tuple, common_tones):
	scale, scalename=scale_tuple
	# Index line (0, 1, 2, ... 22)
	print()
	print_init()
	print(f'{scalename}: {scale}')
	for x in range(0, fbsize+1): print(str(x).center(3 if x==0 else 7, ' '), end='')
	print()
	string(4, scale, common_tones)
	string(11, scale, common_tones)
	string(7, scale, common_tones)
	string(2, scale, common_tones)
	string(9, scale, common_tones)
	string(4, scale, common_tones)

def fretboard_compare(scale_tuple1, scale_tuple2):
	common_tones = [i for i in scale_tuple1[0] if i in scale_tuple2[0]]
	fretboard(scale_tuple1, common_tones)
	fretboard(scale_tuple2, common_tones)
	print()
