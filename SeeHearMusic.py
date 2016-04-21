#!/usr/bin/env python
# -*- coding: utf-8 -*-
import musicDictionary as md
from subprocess import call
import numpy as np
import itertools
import random as rd
from imageData import ImageData

class SeeHearMusic:
	def __init__(self, im, mode, name, instropt):
		self.im = im
		self.name = name
		self.main_staff = ""
		self.secondary_staff = ""
		self.counterpoint_staff = ""
		self.chords_staff = ""
		self.instrument = ""
		self.mode = mode
		self.scale = 0
		self.tempo = 0
		self.notes = ()
		self.colors = [] #Contiene todos los colores de todas las regiones agrupados en una sola lista
		self.bars = [] #Contiene todos los compases con sus dinámicas
		self.finalBars = [] #Contiene todos los compases con dinámicas y notas asignadas
		self.cantusFirmus = [] #Contiene la base para generar la entrada del generador de melodía
		self.instropt = instropt


	#Obtiene la escala dependiendo del matiz promedio
	def getScale(self):
		self.scale = int(self.im.avrHue/30)

	#Obtiene las notas de la escala en el modo definido
	def getScaleNotes(self):
		cycleScale = itertools.cycle(md.scales[self.scale]) #Se cicla la escala para poder recorrerla
		modeScale = list()
		for i in range(self.mode): #Se avanza hasta el primer grado del modo correspondiente
			cycleScale.next()
		for i in range(7):# Se agregan las notas desde la posición definida
			modeScale.append(cycleScale.next())
		#Se ordenan las notas conforme a la jerarquía musical elegida
		self.notes = (modeScale[0],'r',modeScale[4],modeScale[2],'r',modeScale[1],modeScale[3],'r',modeScale[5],modeScale[6])

	#Se crean las dinámicas de los compases dependiendo de la desviación estándar del matiz encontrada en grupos de 7 colores
	#de la lista de todos los colores de todas las regiones
	def createBarsDynamics(self):
		colorIndex = 0
		while colorIndex < len(self.colors):
			#Se toman grupos de 7 colores
			tempColor = self.colors[colorIndex:colorIndex+7]
			tempHues = list()
			#Se obtienen los matices de cada color
			for i in tempColor:
				tempHues.append(self.im.hues[i])
			stdHue = np.std(tempHues)
			#print "stdHue:", stdHue
			#Se elige una de las 8 dinámicas conforme a la desviación estándar del grupo (mínima = dinámica 1....máxima = dinámica 8)
			dynamic = int(stdHue/22.5)
			#print "Dynamic: ", dynamic
			#Se ajusta el índice de color para contar solo el número de tiempo contenidos en la dinámica elegida 
			colorIndex = colorIndex + dynamic +1
			if colorIndex >= len(self.colors): #Caso cuando se llega al final de la lista de colores, se cambia la dinámica por el número de colores que queden
					dynamic = dynamic - (colorIndex - len(self.colors))
					#print "dynamic", dynamic
			self.bars.append(md.rhythm[dynamic][rd.randrange(0,len(md.rhythm[dynamic]))])
			#print md.rhythm[dynamic][0]
			#print "color Index:", colorIndex

	#Asigna a los compases con las dinámicas creadas, notas por cada tiempo que tengan tales compases
	#dependiendo de la jerarquía de cada color se le asigna una nota
	#También se crea el "cantusFirmus" para preparar la entrada del generador de melodía
	def createFinalBars(self):
		colorIndex = 0
		mainMelodyFlag = 0
		soundNoteFlag = 0

		#Se recorren los compases con las dinámicas
		for bar in self.bars:
			tempBar = list()
			for i in range(len(bar)):
				index = 0
				color = self.colors[colorIndex]
				colorIndex+=1
				#print "aquicolorIndex: ", colorIndex
				#Dependiendo de las jerarquías se le asigna la nota correspondiente
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
				tempBar.append(self.notes[index]+str(bar[i])+" ")
				#Preparación de la entrada del AG foox
				#Se toma solo la primera nota (i) del primer self.instrumento (mainMelodyFlag)
				if mainMelodyFlag == 0 and soundNoteFlag == 0:
					if self.notes[index] == 'r' and i == len(bar)-1: #Si existen solo silencios en el compás se agregan un primer grado de la escala
						self.cantusFirmus.append(0)
						print str(tempBar)
						soundNoteFlag = 1
					elif self.notes[index] == 'r': #Se sigue buscando notas al encontrar un silencio
						continue
					else:
						self.cantusFirmus.append(index) #Al encontrar una nota se agrega y se prende la bandera para esperar al siguiente compás
						print str(tempBar)
						soundNoteFlag = 1
			self.finalBars.append(tempBar)
			if mainMelodyFlag == 0: #Se va saltando entre un compás y otro ya que el contrapunto solo se hará para la melodía principal
				mainMelodyFlag = 1
			elif mainMelodyFlag == 1:
				mainMelodyFlag = 0
			soundNoteFlag = 0

	#Asigna compás por compás cada insturmento (main y secondary)
	def createMainStaffs(self):
		self.instrument = 0
		for bar in self.finalBars:
			if self.instrument == 0:
				for note in bar:
					self.main_staff+=note
				self.instrument = 1	
			else:
				for note in bar:
					self.secondary_staff+=note
				self.instrument = 0

	#Se utiliza el programa foox para generar un contrapunto por secciones de diez notas correspondientes a la primera encontrada
	#en cada compás
	def generateCounterpoint(self):
		exactLoop = int(len(self.cantusFirmus)/10)

		for it in range(exactLoop):
			if it == exactLoop-1:
				fooxInput = md.getFooxInput(self.cantusFirmus[it*10:])
			else:
				fooxInput = md.getFooxInput(self.cantusFirmus[it*10:(it+1)*10])
			call ("foox -s 1 -cf "+ fooxInput, shell=True)
			cpf = open("contrapunto.txt", 'r')
			contrapunto = cpf.read()
			self.counterpoint_staff += md.convertFooxOutput(contrapunto, self.notes)
			cpf.close()

	#Utilizando el número de compases de la pieza dados por la longitud del cantusFirmus, se crean acordes de 4to y 5to grado de la 
	#escala base, además del acorde que da el modo
	def generateChordStaff(self):
		progression = itertools.cycle([self.mode+1,self.mode+1,5,5,4,4,self.mode+1,self.mode+1])

		chordBarsIndex = 0
		arpegioFlag = 0
		while chordBarsIndex < len(self.cantusFirmus):
			grade = progression.next()
			chordNotes = md.triadChordMaker(grade, self.scale)
			rhythm = md.chordsrhythm[rd.randrange(0,2)]
			if arpegioFlag == 0:
				for time in rhythm:
					self.chords_staff += md.regularChord(chordNotes, time)
				arpegioFlag = rd.randrange(0,2)
			else:
				for time in rhythm:
					self.chords_staff += md.arpegioChord(chordNotes, time)
				arpegioFlag = 0
			chordBarsIndex+=1

	#Agregar una cadencia final a la pieza, utilizando el 4to y 5to grado de la escala y finalizando en el grado que le da el modo
	def addFinalCadence(self):
		self.main_staff += md.regularChord(md.triadChordMaker(5,self.scale),2) + md.regularChord(md.triadChordMaker(4,self.scale),2) + md.regularChord(md.triadChordMaker(self.mode+1,self.scale),1)
		self.chords_staff += md.regularChord(md.triadChordMaker(5,self.scale),2) + md.regularChord(md.triadChordMaker(4,self.scale),2) + md.regularChord(md.triadChordMaker(self.mode+1,self.scale),1)
		self.counterpoint_staff += md.scales[self.scale][4] + "2 " + md.scales[self.scale][3] + "2 " + md.scales[self.scale][self.mode] + "1 "

	#Definir el tempo de la pieza dependiendo de su luminosidad promedio
	def setTempo(self):
		if self.im.lumAverage < 0.3:
			self.tempo = 60
		else:
			self.tempo = self.im.lumAverage*200

	#Definir el self.instrumento secundario conforme a la saturación promedio de la imagen
	def setInstrument(self):
		if self.im.satAverage <= 0.10:
			self.instrument = "contrabass"
		elif self.im.satAverage <= 0.20:
		 	self.instrument = "cello"
		elif self.im.satAverage <= 0.30:
		 	self.instrument = "viola"
		elif self.im.satAverage <= 0.40:
		 	self.instrument = "xylophone"
		elif self.im.satAverage <= 0.50:
		 	self.instrument = "acoustic guitar (nylon)"
		elif self.im.satAverage <= 0.60:
		 	self.instrument = "violin"
		elif self.im.satAverage <= 0.70:
		 	self.instrument = "french horn"
		elif self.im.satAverage <= 0.80:
		 	self.instrument = "lead 1 (square)"
		elif self.im.satAverage <= 0.90:
		 	self.instrument = "trumpet"
		elif self.im.satAverage <= 1:
		 	self.instrument = "tenor sax"

	#Construir el archivo lilypond final
	def buildLilypondFile(self):
		name = self.name+".ly"
		f = open (name, "w")
		staff = "\\score{\n << \\new Staff \n\\set Staff.instrumentName = #\"Piano  \"\n"
		#staff +="\\set Staff.midiInstrument = #\"piano\"\n"
		staff += "  \\relative c'' {\\tempo 4 = "+str(int(self.tempo))+" \\clef treble " + self.main_staff + "}\n"

		if self.instropt == 0:
			staff +=" \\new Staff \n\\with {midiInstrument = #\""+self.instrument+"\"}  \n"
			staff += "  {\\clef treble " + self.secondary_staff + "}\n"
			staff +=" \\new Staff \n \\with {midiInstrument = #\""+"string ensemble 1"+"\"}  \n"
			staff += "  \\relative c' {\\clef treble " + self.counterpoint_staff + "}\n"
			staff +=" \\new Staff \n\\with {midiInstrument = #\""+"acoustic grand"+"\"}  \n"
			staff += "  {\\clef bass " + self.chords_staff + "}\n"
		elif self.instropt == 1:
			staff +=" \\new Staff \n\\with {midiInstrument = #\""+self.instrument+"\"}  \n"
			staff += "  {\\clef treble " + self.secondary_staff + "}\n"
			staff +=" \\new Staff \n \\with {midiInstrument = #\""+"string ensemble 1"+"\"}  \n"
			staff += "  \\relative c' {\\clef treble " + self.counterpoint_staff + "}\n"
		elif self.instropt == 2:
			staff +=" \\new Staff \n \\with {midiInstrument = #\""+"acoustic grand"+"\"}  \n"
			staff += "  \\relative c' {\\clef treble " + self.counterpoint_staff + "}\n"

		staff += ">>\n\\layout{}\n\\midi{}\n}\n"

		title = "\n\\version \"2.18.2\"\n\\header\n {"
		title += "title = \"TT SEE-HEAR "+self.name+"\""
		title +=  "composer = \"TT SEE-HEAR\"}"
		f.write (title + staff)
		#print title + staff

		f.close()

		call(["lilypond",name])

	#Convertir el archivo midi a wav
	def midiToWav(self):
		call ("timidity -Ow -s 44100 -o "+self.name+".wav "+ self.name+".midi", shell=True)

	def createMusic(self):
		#Obtener la escala dependiendo del matiz promedio
		self.getScale()
		print "Scale:" ,self.scale
		#Obtener las notas de acuerdo a la escala, modo y jerarquía
		self.getScaleNotes()
		print "ScaleNotes:" ,self.notes
		#Juntar todos los colores de todas las regiones 
		self.colors = list(itertools.chain(*self.im.regiones))
		#Crear compases de dinámicas
		self.createBarsDynamics()
		print "Dinámicas:"
		for i in self.bars:
			print i
		#Asignarle notas a cada tiempo definido en los compases de dinámicas así como preparar la entrada del generador de melodía
		self.createFinalBars()
		print "Final Bars:"
		for i in self.finalBars:
			print i
		print "Cantus Firmus", self.cantusFirmus
		#Asignar el contenido de los primeros dos self.instrumentos
		self.createMainStaffs()
		print "Main instrument:", self.main_staff
		print "Secondary instrument:", self.secondary_staff
		#Generar el contrapunto correspondiente a la primer melodía (main)
		self.generateCounterpoint()
		print "Counterpoint Staff:", self.counterpoint_staff
		#Generar el contenido del self.instrumento de acordes
		self.generateChordStaff()
		print "Chords Staff:", self.chords_staff
		#Agregar cadencia final
		self.addFinalCadence()
		#Definir tempo de la pieza
		self.setTempo()
		print "Tempo:", self.tempo
		#Definir self.instrumento secundario
		self.setInstrument()
		print "Secondary Instrument:", self.instrument
		#Construir el archivo lilypond final
		self.buildLilypondFile()
		#Convertir midi a wav
		self.midiToWav()








