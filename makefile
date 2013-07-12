edit:
	geany *.py modules/*.py websites/*.py README.md makefile&

clean:
	rm -f html/*.html
	./fetchLink.py history clear
