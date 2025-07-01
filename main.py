#!/bin/env python3
from fretboard import fretboard

def fretboard_compare(scale1, scale2):
	fretboard(scale1)
	fretboard(scale2)

c_maj = [0, 2, 4, 5, 7, 9, 11]
c_min = [0, 2, 3, 5, 7, 8, 10]
fretboard_compare(c_maj, c_min)

print()
