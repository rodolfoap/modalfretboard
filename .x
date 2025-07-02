case "$1" in
e)	vi -p main.py fretboard.py print_center.py scale_gen.py
	;;
"")	./main.py C aeolian Eb dorian
	;;
esac
