import colorsys
import time
import numpy as np
import Image

image=Image.open("birll.jpg")

pixels = list(image.getdata())
pixelsHsl = []
hue = []
light = []
sat = []
for pix in pixels:
	r,g,b=pix
	r,g,b=[x/255.0 for x in r, g, b]
	h,l,s=colorsys.rgb_to_hls(r,g,b)
	h=h*360
	hslpix=(h,l,s)
	hue.append(h)
	light.append(l)
	sat.append(s)
	pixelsHsl.append(hslpix)

print "**************Matiz:***************" 
print "Minimo Matiz:" 
print np.amin(hue)
print "Maximo Matiz: "
print np.amax(hue)
print "Promedio Matiz"
print np.average(hue)
print "Mediana Matiz"
print np.mean(hue)
print "Desv. Estandar Mariz"
print np.std(hue)

print "**************Luminosidad:***************" 
print "Minimo Luminosidad:" 
print np.amin(light)
print "Maximo Luminosidad: "
print np.amax(light)
print "Promedio Luminosidad"
print np.average(light)
print "Mediana Luminosidad"
print np.mean(light)
print "Desv. Estandar Mariz"
print np.std(light)

print "**************Saturacion:***************" 
print "Minimo Saturacion:" 
print np.amin(sat)
print "Maximo Saturacion: "
print np.amax(sat)
print "Promedio Saturacion"
print np.average(sat)
print "Mediana Saturacion"
print np.mean(sat)
print "Desv. Estandar Mariz"
print np.std(sat)