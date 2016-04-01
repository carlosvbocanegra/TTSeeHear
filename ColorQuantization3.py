#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('/usr/lib64/python2.7/site-packages')
import numpy as np
import cv2
import colorsys
import time
#import Image
from PIL import Image

img = cv2.imread('brill.jpg')
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

K = 12 # number of colors 
compactness, labels, centers = cv2.kmeans(Z,https://docs.google.com/spreadsheets/d/1zMoX1cR_Ck-pqZ2frdX1QRTWs8caer37wyYx6CVqtF0/edit?usp=sharing K, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
centers = np.uint8(centers)
res = centers[labels.flatten()]
res2 = res.reshape((img.shape))


imageWidth = res2.shape[1] #Get image width
imageHeight = res2.shape[0] #Get image height

print imageWidth, imageHeight

total = imageWidth * imageHeight


colors, times, rates = [], [], []

def remember(pixel):
	if pixel in colors:	
		times[colors.index(pixel)] += 1
	else:
		colors.append(pixel) # BGR
		times.append(1)			
	

for x in range(imageWidth):
	for y in range(imageHeight):
		remember( res2[y,x].tolist() )

colors2 = colors

print "Colores (BGR): \n", colors2 # BGR

var = []		
for i in range(len(times)):
	var.append(times[i] / float(total)) # percentages
	var.append(colors[i]) 
	rates.append(var)
	var = [] 		
	
rates.sort(reverse=True)

colors, regiones = [], []

def memory(pixel):
	for i in range(len(rates)):
		if pixel == rates[i][1]:
			if i in colors:
				pass
			else:	
				colors.append(i)	

n = 8 # raíz cuadrada del número de regiones

for i in range(n):
	for j in range(n):
		for y in range(imageHeight / n): # rows
			for x in range(imageWidth / n): # columns
				memory( res2[(i * (imageHeight / n) ) + y, (j * (imageWidth / n)) + x].tolist() )
		#print colors
		list(set(colors))
		#print colors
		regiones.append(colors)
		colors = []	

for i in colors2: # BGR to RGB
	i.reverse()
	
colors = colors2
			
print "Colores (RGB): \n", colors # RGB
print "Ocurrencia de los colores: \n", times
print "Colores ordenados por porcentajes: \n", rates	# percentages and colors by magnitude
print "Regiones: \n", regiones # posición en rates de los colores presentes en cada región

image=Image.open("sterrennacht.jpg")

pixels = list(image.getdata())
pixelsHsl = []
hue = []
light = []
sat = []
for pix in pixels:
	r, g, b = pix
	r, g, b = [ x / 255.0 for x in r, g, b]
	h, l, s = colorsys.rgb_to_hls(r, g, b)
	h = h * 360
	hslpix = (h, l, s)
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
				
#"""https://docs.google.com/spreadsheets/d/1zMoX1cR_Ck-pqZ2frdX1QRTWs8caer37wyYx6CVqtF0/edit?usp=sharing
cv2.imshow('res2',res2)

w = cv2.waitKey(0) & 0xFF # for 64-bit machine
if w == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif w == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('sterrennachtKmeans.jpg', res2)
#"""   
