case "$1" in
e)	vi -p modalfretboard.py fretboard.py print_center.py scale_gen.py
	;;
"")	./modalfretboard.py C aeolian Eb dorian
	;;
esac
