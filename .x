case "$1" in
e)	vi -p cline.py
	# main.py fretboard.py print_center.py scale_gen.py
	;;
"")	./cline.py
	#./main.py C aeolian Eb dorian
	;;
esac
