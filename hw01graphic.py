fname= "work01.ppm"

height = 500
width = 500
ftype = "P3"


def write_header(f,w,h):
	f.write("%s\n" % (ftype))
	f.write("%d %d\n" % (w, h)) 
	f.write("255\n")

def color(f,w,h):
	wi = 0
	hi = 0
	for each in range(w):
		if wi < 100 and hi <50:
			for other in range(h):
				f.write("255 215 0 ")
				hi+=1
		else:
			for other in range(h):
				f.write("0 191 255 ")
				hi+=1
		wi+=1
		hi = 0


with open(fname,"w") as file:
	write_header(file,width,height)
	color(file,width,height)