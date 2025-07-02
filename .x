case "$1" in
e)	vi -p modalfretboard fretboard.py print_center.py scale_gen.py
	;;
"")	./modalfretboard C aeolian Eb dorian
	;;
esac
