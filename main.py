#!/bin/env python3
from fretboard import fretboard
from scale_gen import get_scale

def fretboard_compare(scale1, scale2):
	fretboard(scale1)
	fretboard(scale2)

fretboard_compare(get_scale('C', 'aeolian'), get_scale('D#', 'dorian'))

print()
