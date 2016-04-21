#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools

scales = [
#C Major
['c','d','e','f','g','a','b'],
# C# Major
#cs = [cis,dis,eis,fis,gis,ais,bis]
# Db Major
['des','ees','f','ges','aes','bes','c'],
#D Major
['d','e','fis','g','a','b','cis'],
# Eb Major
['ees','f','g','aes','bes','c','d'],
#E Major
['e','fis','gis','a','b','cis','dis'],
# F Major
['f','g','a','bes','c','d','e'],
# F# MajorModerato
#fs = [fis,gis,ais,b,cis,dis,eis]
# Gb Major
['ges','aes','bes','ces','des','ees','f'],
#G Major
['g','a','b','c','d','e','fis'],
# Ab Major
['aes','bes','c','des','ees','f','g'],
#A Major
['a','b','cis','d','e','fis','gis'],
# Bb Major
['bes','c','d','ees','f','g','a'],
#B Major
['b','cis','dis','e','fis','gis','ais'],
# Cb Major
#cf = [ces,des,ees,fes,ges,aes,bes]
]

rhythm = [[[1]], 
		[[2, 2]],
		[[2, 4, 4], [4, 2, 4], [4, 4, 2]],
		[[2, 4, 8, 8], [2, 8, 4, 8], [2, 8, 8, 4], [4, 2, 8, 8], [4, 8, 2, 8], [4, 8, 8, 2], [8, 2, 4, 8], [8, 2, 8, 4], [8, 4, 2, 8], [8, 4, 8, 2], [8, 8, 2, 4], [8, 8, 4, 2], [4, 4, 4, 4]],
		[[2, 8, 8, 8, 8], [8, 2, 8, 8, 8], [8, 8, 2, 8, 8], [8, 8, 8, 2, 8], [8, 8, 8, 8, 2], [4, 4, 4, 8, 8], [4, 4, 8, 4, 8], [4, 4, 8, 8, 4], [4, 8, 4, 4, 8], [4, 8, 4, 8, 4], [4, 8, 8, 4, 4], [8, 4, 4, 4, 8], [8, 4, 4, 8, 4], [8, 4, 8, 4, 4], [8, 8, 4, 4, 4]],
		[[4, 4, 8, 8, 8, 8], [4, 8, 4, 8, 8, 8], [4, 8, 8, 4, 8, 8], [4, 8, 8, 8, 4, 8], [4, 8, 8, 8, 8, 4], [8, 4, 4, 8, 8, 8], [8, 4, 8, 4, 8, 8], [8, 4, 8, 8, 4, 8], [8, 4, 8, 8, 8, 4], [8, 8, 4, 4, 8, 8], [8, 8, 4, 8, 4, 8], [8, 8, 4, 8, 8, 4], [8, 8, 8, 4, 4, 8], [8, 8, 8, 4, 8, 4], [8, 8, 8, 8, 4, 4]],
		[[4, 4, 8, 8, 8, 8], [4, 8, 4, 8, 8, 8], [4, 8, 8, 4, 8, 8], [4, 8, 8, 8, 4, 8], [4, 8, 8, 8, 8, 4], [8, 4, 4, 8, 8, 8], [8, 4, 8, 4, 8, 8], [8, 4, 8, 8, 4, 8], [8, 4, 8, 8, 8, 4], [8, 8, 4, 4, 8, 8], [8, 8, 4, 8, 4, 8], [8, 8, 4, 8, 8, 4], [8, 8, 8, 4, 4, 8], [8, 8, 8, 4, 8, 4], [8, 8, 8, 8, 4, 4]],
		[[8, 8, 8, 8, 8, 8, 8, 8]]]

chordsrhythm = [["2.","4"],["1"]]


def getFooxInput(cantusFirmus):
	intervalsEquivalent = {
	0:1,
	2:5,
	3:3,
	5:2,
	6:4,
	8:6,
	9:7
	}
	fooxInput = ""
	for note in cantusFirmus:
		fooxInput += str(intervalsEquivalent[note] + 3)+ " "
	return fooxInput

def convertFooxOutput(contrapunto, notes):
	fooxEquivalent = {
	'c':0,
	'd':5,
	'e':3,
	'f':6,
	'g':2,
	'a':8,
	'b':9
	}
	auxcount = 0
	contrapunto_staff = ""
	for note in contrapunto:
		if note == '\'' or note == '1' or note == 'i' or note == 's' or note == ' ':
			continue
		else:
			auxcount +=1
			contrapunto_staff += notes[fooxEquivalent[note]] + '1 '
	#print "auxcount: ", auxcount
	return contrapunto_staff

def triadChordMaker(grade, scale):
	chordNotes = list()
	root = ""
	third = ""
	fifth = ""
	baseScale = itertools.cycle(scales[scale]) #Ciclar la escala
	for i in range(grade): #Avanzar hasta el grado deseado
		root = baseScale.next()
	for i in range(2):
		third = baseScale.next()
	for i in range(2):
		fifth = baseScale.next()
	chordNotes.append(root)
	chordNotes.append(third)
	chordNotes.append(fifth)
	return chordNotes

def regularChord(chordNotes, time):
	chord = " <"+chordNotes[0]+" "+chordNotes[1]+" "+chordNotes[2]+">"+str(time)+" "
	return chord

def arpegioChord(chordNotes, time):
	chord = " \\set tieWaitForNote = ##t "
	chord += "\\grace { "+chordNotes[0]+"32 ~ "+chordNotes[1]+" ~ "+chordNotes[2]+" ~ "+chordNotes[0]+" ~ } "
	chord +="<"+chordNotes[0]+" "+chordNotes[1]+" "+chordNotes[2]+" "+chordNotes[0]+">"+str(time)+" \\unset tieWaitForNote "
	return chord


# 1
# 2
# 4
# 8
# 2. 
# 4.
# 8.

# 1
# 0.5
# 0.25
# 0.125
# 0.75
# 0.375
# 0.1875





