import sys
from fretboard import chromatic, modes # fretboard_compare, fretboard, 

def usage(message=''):
	exit(f'''
Usage:
        {sys.argv[0]} [TONE1 MODE1 [TONE2 MODE2], ... ]

Example:
        {sys.argv[0]} C aeolian Eb dorian # Which is the Blue Bossa modulation

All tones should be expressed in uppercase with flats (e.g. _Eb_ instead of _D#_).

Available tones are: {chromatic}
Available modes are: {list(modes.keys())}
{message}''');

def print_headers():
	print('\nCommand was:', ' '.join(sys.argv))
	print('Tones in red are common to both scales.')

def get_pairs():
	scales=[]
	for x in range(len(sys.argv[1:])//2):
		scale_key, scale_mode=sys.argv[x*2+1], sys.argv[x*2+2] 
		# instead C#, Cs can be used in the command line
		if scale_key.endswith('s'): scale_key=scale_key.replace('s', '#')
		if scale_key not in chromatic: usage(f'\n[ERROR] Tone "{scale_key}" does not exist in {chromatic}\n')
		if scale_mode not in list(modes.keys()): usage(f'\n[ERROR] Mode "{scale_mode}" does not exist in {list(modes.keys())}\n')
		scales.append((scale_key, scale_mode))
	return scales
	# scales == [('a', 'ionian'), ('c', 'diorian'), ('j', 'pripipilian')]

