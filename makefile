all: hw01graphic.py
	python hw01graphic.py
	convert hw01.ppm hw01.png
clean:
	rm -rf hw01.ppm