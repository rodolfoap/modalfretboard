#!/bin/env python3
from fretboard import fretboard_compare
from scale_gen import get_scale
import sys

if len(sys.argv)<5: exit(f'''
Usage:
        {sys.argv[0]} [TONE1 MODE1 TONE2 MODE2]

Example:
        {sys.argv[0]} C aeolian Eb dorian # Which is the Blue Bossa modulation

All tones should be expressed in uppercase with flats (e.g. _Eb_ instead of _D#_).

Available modes are: ionian, dorian, phrygian, lydian, mixolydian, aeolian, locrian
''');
print('\nCommand was:', sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] )
print('Tones in red are common to both scales.')
fretboard_compare(get_scale(sys.argv[1], sys.argv[2]), get_scale(sys.argv[3], sys.argv[4]))
