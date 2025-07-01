#!/bin/env python3
def fretboard(scale_intervals):
	strings = [
		['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E'],
		['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A'],
		['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D'],
		['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G'],
		['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
		['e', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E']
	]

	note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
	scale_notes = [note_names[i % 12] for i in scale_intervals]
	fretboard = ""
	for string in strings:
		for fret in range(13):  # Display up to the 12th fret
			note = string[fret]
			if note.upper() in scale_notes:
				fretboard += f"{note:2} "
			else:
				fretboard += "-- "
		fretboard += "\n"
	print(fretboard)

c_maj = [0, 2, 4, 5, 7, 9, 11]
fretboard(c_maj)
