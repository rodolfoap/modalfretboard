#!/bin/env python3
from fretboard import fretboard
from scale_gen import get_scale

def fretboard_compare(scale1, scale2):
	common_tones = [i for i in scale1 if i in scale2]
	fretboard(scale1, common_tones)
	fretboard(scale2, common_tones)

fretboard_compare(get_scale('C', 'aeolian'), get_scale('D#', 'dorian'))

print()
