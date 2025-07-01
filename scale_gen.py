#!/bin/env python3
from fretboard import chromatic, modes, natscale

def get_scale(tonic_name, mode_name):
	""" First, get the relative degrees """

	# 5 (aeolian is the 6th degree of natscale)
	natural_degree=natscale.index(modes[mode_name]) 

	# [9, 11, 0, 2, 4, 5, 7] == A Aeolian
	modulation=natscale[natural_degree:]+natscale[:natural_degree]

	# modulation has the right scale structure (tones, semi-tones)
	# but it starts in A; how many semitones to go back to C?
	tonicnote=modulation[0] # 9

	# So, let's transpose down the rotated natural scale nine semitones
	# [0, 2, 3, 5, 7, 8, 10] == C Aeolian
	intervals=[(x+12-tonicnote)%12 for x in modulation]

	""" Second, apply the structure to the rotated chromatic scale"""

	# 2, D is the 0,1,2nd of notnames
	scale_shift=chromatic.index(tonic_name.upper())
	# ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#']
	chromatic_shifted=chromatic[scale_shift:]+chromatic[:scale_shift]

	# ['D', 'E', 'F', 'G', 'A', 'A#', 'C'] # D aeolian
	chromatic_shifted_names=[chromatic_shifted[i] for i in intervals]
	return chromatic_shifted_names

# print(get_scale('D', 'aeolian'))
