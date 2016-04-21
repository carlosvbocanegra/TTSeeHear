#!/usr/bin/env python
# -*- coding: utf-8 -*-
import imageDatared as im
import musicDictionary as md
from subprocess import call
import numpy as np
import itertools
import contrapunto as cp
import random as rd
# ------------------NEW ---------------------------------#
mode = 6

#scale = int(im.avrHue/30)
scale = 0
print "Scale: ", scale
if mode == 0:
	notes = (md.scales[scale][0],'r',md.scales[scale][4],md.scales[scale][2],'r',md.scales[scale][1],md.scales[scale][3],'r',md.scales[scale][5],md.scales[scale][6])
elif mode == 1:	
	notes = (md.scales[scale][1],'r',md.scales[scale][5],md.scales[scale][3],'r',md.scales[scale][2],md.scales[scale][4],'r',md.scales[scale][6],md.scales[scale][0])
elif mode == 2:
	notes = (md.scales[scale][2],'r',md.scales[scale][6],md.scales[scale][4],'r',md.scales[scale][3],md.scales[scale][5],'r',md.scales[scale][0],md.scales[scale][1])
elif mode == 3:
	notes = (md.scales[scale][3],'r',md.scales[scale][0],md.scales[scale][5],'r',md.scales[scale][4],md.scales[scale][6],'r',md.scales[scale][1],md.scales[scale][2])
elif mode == 4:
	notes = (md.scales[scale][4],'r',md.scales[scale][1],md.scales[scale][6],'r',md.scales[scale][5],md.scales[scale][0],'r',md.scales[scale][2],md.scales[scale][3])
elif mode == 5:	
	notes = (md.scales[scale][5],'r',md.scales[scale][2],md.scales[scale][0],'r',md.scales[scale][6],md.scales[scale][1],'r',md.scales[scale][3],md.scales[scale][4])
elif mode == 6:
	notes = (md.scales[scale][6],'r',md.scales[scale][3],md.scales[scale][1],'r',md.scales[scale][0],md.scales[scale][2],'r',md.scales[scale][4],md.scales[scale][5])

intervalsEquivalent = {
	0:1,
	2:5,
	3:3,
	5:2,
	6:4,
	8:6,
	9:7
}

fooxEquivalent = {
	'c':0,
	'd':5,
	'e':3,
	'f':6,
	'g':2,
	'a':8,
	'b':9
}

def triadChordMaker(grade, scale):
	chordNotes = list()
	root = ""
	third = ""
	fifth = ""
	baseScale = itertools.cycle(md.scales[scale]) #Ciclar la escala
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

def getFooxInput(cantusFirmus):
	fooxInput = ""
	for note in cantusFirmus:
		fooxInput += str(intervalsEquivalent[note] + 3)+ " "
	return fooxInput


def convertFooxOutput(contrapunto):
	auxcount = 0
	contrapunto_staff = ""
	for note in contrapunto:
		if note == '\'' or note == '1' or note == 'i' or note == 's' or note == ' ':
			continue
		else:
			auxcount +=1
			contrapunto_staff += notes[fooxEquivalent[note]] + '1 '
	print "auxcount: ", auxcount
	return contrapunto_staff

f = open ("meloB.ly", "w")

upper_staff = ""
lower_staff = ""
instrument = 0

colors = list(itertools.chain(*im.regiones))
#print colors

colorIndex = 0
bars = list()

while colorIndex < len(colors):
	tempColor = colors[colorIndex:colorIndex+7]
	tempHues = list()
	for i in tempColor:
		tempHues.append(im.hues[i])
	stdHue = np.std(tempHues)
	#print "stdHue:", stdHue
	dynamic = int(stdHue/22.5)
	#print "Dynamic: ", dynamic
	colorIndex = colorIndex + dynamic +1
	if colorIndex >= len(colors):
			dynamic = dynamic - (colorIndex - len(colors))
			#print "dynamic", dynamic
	bars.append(md.rhythm[dynamic][rd.randrange(0,len(md.rhythm[dynamic]))])
	#print md.rhythm[dynamic][0]
	#print "color Index:", colorIndex


for i in bars:
	print i, "\n"

#print "color Index:", colorIndex

#print "bars len:", len(list(itertools.chain(*bars)))
#print "colors len:", len(colors)

colorIndex = 0
finalBars = list()

mainMelodyFlag = 0
soundNoteFlag = 0
cantusFirmus = list()

for bar in bars:
	tempBar = list()
	for i in range(len(bar)):
		index = 0
		color = colors[colorIndex]
		colorIndex+=1
		#print "aquicolorIndex: ", colorIndex
		if color <=2:
			index=0
		elif color <=3:
			index=1
		elif color <=5:
			index=2
		elif color <=7:
			index=3
		else:
			index=color-4
		tempBar.append(notes[index]+str(bar[i])+" ")
		#Preparación de la entrada del AG foox
		#Se toma solo la primera nota (i) del primer instrumento (mainMelodyFlag)
		if mainMelodyFlag == 0 and soundNoteFlag == 0:
			if notes[index] == 'r' and i == len(bar)-1:
				cantusFirmus.append(0)
				print str(tempBar)
				soundNoteFlag = 1
			elif notes[index] == 'r':
				continue
			else:
				cantusFirmus.append(index)
				print str(tempBar)
				soundNoteFlag = 1
	finalBars.append(tempBar)
	if mainMelodyFlag == 0:
		mainMelodyFlag = 1
	elif mainMelodyFlag == 1:
		mainMelodyFlag = 0
	soundNoteFlag = 0

print "FinalBars len:", len(finalBars)
#print "FinalBars len:", len(list(itertools.chain(*finalBars)))
for bar in finalBars:
	if instrument == 0:
		print bar
		for note in bar:
			upper_staff+=note
		instrument = 1	
	else:
		for note in bar:
			lower_staff+=note
		instrument = 0
	#print bar


print "cantusFirmus", cantusFirmus
print "Cantus Firmus len:", len(cantusFirmus)

exactLoop = int(len(cantusFirmus)/10)
print "Exact Loop:", exactLoop

contrapunto_staff = ""

for it in range(exactLoop):
	if it == exactLoop-1:
		fooxInput = getFooxInput(cantusFirmus[it*10:])
	else:
		fooxInput = getFooxInput(cantusFirmus[it*10:(it+1)*10])
	call ("foox -s 1 -cf "+ fooxInput, shell=True)
	cpf = open("contrapunto.txt", 'r')
	contrapunto = cpf.read()
	contrapunto_staff += convertFooxOutput(contrapunto)
	cpf.close()

chords_staff = ""

progression = itertools.cycle([mode+1,mode+1,5,5,4,4,mode+1,mode+1])

chordBarsIndex = 0
arpegioFlag = 0
while chordBarsIndex < len(cantusFirmus):
	grade = progression.next()
	chordNotes = triadChordMaker(grade, scale)
	rhythm = md.chordsrhythm[rd.randrange(0,2)]
	if arpegioFlag == 0:
		for time in rhythm:
			chords_staff += regularChord(chordNotes, time)
		arpegioFlag = rd.randrange(0,2)
	else:
		for time in rhythm:
			chords_staff += arpegioChord(chordNotes, time)
		arpegioFlag = 0
	chordBarsIndex+=1

#Ending cadence
upper_staff += regularChord(triadChordMaker(5,scale),2) + regularChord(triadChordMaker(4,scale),2) + regularChord(triadChordMaker(mode+1,scale),1)
chords_staff += regularChord(triadChordMaker(5,scale),2) + regularChord(triadChordMaker(4,scale),2) + regularChord(triadChordMaker(mode+1,scale),1)
contrapunto_staff += md.scales[scale][4] + "2 " + md.scales[scale][3] + "2 " + md.scales[scale][mode] + "1 "


if im.lumAverage < 0.3:
	tempo = 60
else:
	tempo = im.lumAverage*200


instrument = ""
#Instruments:
if im.satAverage <= 0.20:
	instrument = "contrabass"
elif im.satAverage <= 0.30:
 	instrument = "cello"
elif im.satAverage <= 0.40:
 	instrument = "xylophone"
elif im.satAverage <= 0.50:
 	instrument = "acoustic guitar (nylon)"
elif im.satAverage <= 0.60:
 	instrument = "string ensemble 1"
elif im.satAverage <= 0.70:
 	instrument = "french horn"
elif im.satAverage <= 0.80:
 	instrument = "lead 1 (square)"
elif im.satAverage <= 1:
 	instrument = "tenor sax"
#contrabass
#cello
#trombone
#xylophone
#acoustic guitar (nylon)
#string ensemble 1
#french horn
#lead 1 (square)
#tenor sax

staff = "\\score{\n << \\new Staff \n\\set Staff.instrumentName = #\"Piano  \"\n"
#staff +="\\set Staff.midiInstrument = #\"piano\"\n"
staff += "  \\relative c'' {\\tempo 4 = "+str(int(tempo))+" \\clef treble " + upper_staff + "}\n"

staff +=" \\new Staff \n\\with {midiInstrument = #\""+instrument+"\"}  \n"
staff += "  {\\clef treble " + lower_staff + "}\n"

staff +=" \\new Staff \n \\with {midiInstrument = #\""+"string ensemble 1"+"\"}  \n"
staff += "  \\relative c' {\\clef treble " + contrapunto_staff + "}\n"

staff +=" \\new Staff \n\\with {midiInstrument = #\""+"Acoustic Grand Piano"+"\"}  \n"
staff += "  {\\clef bass " + chords_staff + "}\n"

staff += ">>\n\\layout{}\n\\midi{}\n}\n"

title = """\n\\version "2.18.2"\n\\header\n {
  title = "TT SEE-HEAR"
  composer = "Python"
  tagline = "Copyright: -"
}"""

f.write (title + staff)
#print title + staff

f.close()

call(["lilypond","meloB.ly"])
#call(["timidity","meloB.midi"])




