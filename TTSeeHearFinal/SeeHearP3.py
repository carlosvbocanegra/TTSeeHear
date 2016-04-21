#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
#sys.path.append('/usr/lib64/python2.7/site-packages')
import numpy as np
import cv2
import colorsys
import time
from PIL import Image
import matplotlib.pyplot as plt
from subprocess import call
from imageData import ImageData

def getImageData(imageFileName):
	img = cv2.imread(imageFileName)
	Z = img.reshape((-1,3))

	# convert to np.float32
	Z = np.float32(Z)

	# define criteria, number of clusters(K) and apply kmeans()
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

	K = 14 # number of colors 
	compactness, labels, centers = cv2.kmeans(Z, K, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

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

	#print "Colores (BGR): \n", colors2 # BGR

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

	n = 4 # raíz cuadrada del número de regiones



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
				
	# print "Colores (RGB): \n", colors # RGB
	# print "Ocurrencia de los colores: \n", times
	# print "Colores ordenados por porcentajes: \n", rates	# percentages and colors by magnitude
	# print "Regiones: \n", regiones # posición en rates de los colores presentes en cada región

	#""" barchart rates
	percentages = []

	ind = np.arange(K)  # the x locations for the groups
	width = 0.4       # the width of the bars

	fig, ax = plt.subplots()

	w = 0
	rects = []
	labels = []
	colour = []
	aux = []
	c = 'C'

	for i in rates:
		percentages.append(i[0] * 100)
		for j in i[1]:
			aux.append(j / 255.0) 
		#color: you can pass an R , G , B tuple, where each of R , G , B are in the range [0,1]
		colour.append(list(aux))
		aux = [] 
		#handle.append(rects[0])
		labels.append(c + str(w + 1))
		j += 1
		w += 1
		#autolabel(rects)

	#print "colour"	
	#print colour

		
		
	rects = ax.bar(ind, percentages, width, color = "k")	
		
	for i in range(len(colour)):
		rects[i].set_color(colour[i])		


	# add some text for labels, title and axes ticks
	ax.set_ylabel('Porcentajes')
	ax.set_xlabel('Colores')
	ax.set_title('Colores representativos de la imagen')
	ax.set_xticks(ind + width / 2.0)
	ax.set_xticklabels(labels)		


	#handle, legend = [], []
	#legend.append('Colores representativos')
	#ax.legend(handle, legend)

	def autolabel(rects):
	    # attach some text labels
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x() + rect.get_width() / 2.0, 1.05 * height,
	                '%.2f' % height,
	                ha='center', va='bottom')

	autolabel(rects)

	#plt.show()
	#"""

	image=Image.open(imageFileName)

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

	hues = []
	for item in colors:
		r,g,b = item
		r,g,b = [ x / 255.0 for x in r, g, b]
		h,s,l = colorsys.rgb_to_hls(r, g, b)
		h = h * 360
		if h < 25:
			h = 335 + h
		else:
			h = h - 25
		hues.append(h)

	# print "**************Matiz:***************" 
	# print "imageFileNamemo Matiz:" 
	# print np.amin(hue)
	# print "Maximo Matiz: "
	# print np.amax(hue)
	# print "Promedio Matiz"
	# print np.average(hue)
	# print "Mediana Matiz"
	# print np.mean(hue)
	# print "Desv. Estandar Matiz"
	# print np.std(hue)

	# print "**************Luminosidad:***************" 
	# print "imageFileNamemo Luminosidad:" 
	# print np.amin(light)
	# print "Maximo Luminosidad: "
	# print np.amax(light)
	# print "Promedio Luminosidad"
	# print np.average(light)
	# print "Mediana Luminosidad"
	# print np.mean(light)
	# print "Desv. Estandar Luminosidad"
	# print np.std(light)

	# print "**************Saturacion:***************" 
	# print "imageFileNamemo Saturación:" 
	# print np.amin(sat)
	# print "Maximo Saturación: "
	# print np.amax(sat)
	# print "Promedio Saturación"
	# print np.average(sat)
	# print "Mediana Saturación"
	# print np.mean(sat)
	# print "Desv. Estandar Saturación"
	# print np.std(sat)
					
	#"""
	# cv2.imshow('res2',res2)

	# w = cv2.waitKey(0) & 0xFF # for 64-bit machine
	# if w == 27:         # wait for ESC key to exit
	#     cv2.destroyAllWindows()
	# elif w == ord('s'): # wait for 's' key to save and exit
	#     cv2.imwrite('imageFileNameKmeans.jpg', res2)
	#"""   

	imageData = ImageData()
	imageData.hues = hues
	imageData.colores = colors
	imageData.regiones= regiones
	imageData.satAverage = np.average(sat)
	imageData.lumAverage = np.average(light)
	imageData.desvHue = np.std(hue)
	imageData.avrHue = np.average(hue)
	return imageData

if __name__ == '__main__':
	im = getImageData("lisa.jpg")
	print im.hues
	print im.colores
	print im.regiones
	print im.satAverage
	print im.lumAverage
	print im.desvHue
	print im.avrHue
