#!/usr/bin/env python
# -*- coding: utf-8 -*-
import imageData as im
import musicDictionary as md
from subprocess import call
import numpy as np
import itertools
# ------------------NEW ---------------------------------#

#notes = ("\\absolute c1 ","\\absolute e2 ","\\absolute g2 ","\\absolute d8 ","\\absolute f8 ","\\absolute a8 ","\\absolute b8 ", "\\absolute cis16 ", "\\absolute dis16 ", "\\absolute eis16 ", "\\absolute fis16 ", "\\absolute gis16 ", "\\absolute ais16 ")
#notes = ("\\absolute c1 ","\\absolute e2 ","\\absolute g2 ","\\absolute d8 ","\\absolute f8 ","\\absolute a8 ","\\absolute b8 ", "c'8 ", "d' d8 ", "e'8 ", "f'8 ", "g'16 ", "a'8 ")
#notes = ("c1 ","e2 ","g2 ","d8 ","f8 ","a8 ","b8 ", "c'8 ", "d' d8 ", "e'8 ", "f'8 ", "g'16 ", "a'8 ")
#notes = ("c1 ","c2 ", "c4 ", "c8 ","r2 ","e1 ","e2 ","e4 ","e8 ","r4 ","g1 ","g2 ","g4 ","g8 ","r4 ","d1 ","d2 ","d4 ","d8 ","r8 ","f1 ","f2 ","f4 ","f8 ","r8 ","a1 ","a2 ","a4 ","a8 ","r8 ","b1 ","b2 ","b4 ","b8 ","r8 ")

mode = 6

scale = 5

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

f = open ("melo.ly", "w")

upper_staff = ""
lower_staff = ""
instrument = 0

#colors = itertools.chain(*regiones)




for region in im.regiones:	
	for color in region:
		index = 0
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
		if instrument == 0:
			upper_staff+=notes[index]+" "
			instrument = 1
		else:
			lower_staff+=notes[index]+" "
			instrument = 0

if im.lumAverage < 0.225:
	tempo = 40
else:
	tempo = im.lumAverage*200


#print tempo
# if im.lumAverage <= 0.20:
# #Lento (45-60)
# 	tempo = im.lumAverage*300
# elif im.lumAverage <= 0.40:
# #Adagio (66 - 76)
# 	tempo = im.lumAverage*190
# elif im.lumAverage <= 0.60:
# #Andante (76-108)
# 	tempo = 
# elif im.lumAverage <= 0.80:
# #Allegro (120-168)
# 	tempo = "Allegro"
# elif im.lumAverage <= 1:
# #Presto (168-200)
# 	tempo = "Presto"

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
staff += "  {\\tempo 4 = "+str(int(tempo))+" \\clef treble " + upper_staff + "}\n"

staff +=" \\new Staff \n\\with {midiInstrument = #\""+instrument+"\"}  \n"
staff += "  {\\clef treble " + lower_staff + "}\n"

staff += ">>\n\\layout{}\n\\midi{}\n}\n"

title = """\n\\version "2.18.2"\n\\header\n {
  title = "TT SEE-HEAR"
  composer = "Python"
  tagline = "Copyright: -"
}"""

f.write (title + staff)
#print title + staff

f.close()

call(["lilypond","melo.ly"])
call(["timidity","melo.midi"])

