#!/bin/env python3
import sys
from fretboard import fretboard_compare, fretboard, chromatic
from scale_gen import get_scale
from helpers import usage, get_pairs, print_headers

if len(sys.argv) <3 or len(sys.argv)%2==0: usage()
scales=get_pairs()
print_headers()

if len(scales)==1:
	fretboard(get_scale(scales[0][0], scales[0][1]), chromatic)
	print()
else:
	for i in range(len(scales)-1): 
		print('='*158)
		fretboard_compare(get_scale(scales[i][0], scales[i][1]), get_scale(scales[i+1][0], scales[i+1][1]))
