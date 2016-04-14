#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


chords = [
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
		[8, 8, 8, 8, 8, 8, 8, 8]]
