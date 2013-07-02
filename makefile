edit:
	geany *.py modules/*.py websites/*.py README.md makefile&

clean:
	rm html/*.html
	./fetchLink.py history clear
