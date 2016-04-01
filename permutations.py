#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools # to remove permutation duplicates

print "Introduzca la cantidad de notas del compás (1-8):"
n = int( raw_input() )

#print isinstance( n, ( int, long ) )
#print type(n)


def permute( x ):
	l = len( x )

	if l == 1:
		return x
	
	z = []
		
	for i in range( l ):
		aux = x[:]
		aux.pop( i )
		y = permute( aux )

		for j in y:
			aux2 = list( x[i:i + 1] )
			if isinstance( j, ( list ) ):
				aux2 += j
			else:	
				aux2.append( j )
			
			z.append( aux2 )
				
	return z
	
def remove_duplicates(l):
	l.sort()
	return [ i for i,_ in itertools.groupby( l ) ]
		
	
if n == 1:
	#partition = [1]
	permutations = [1]
elif n == 2:
	#partition = [2, 2]
	permutations = [2, 2]
elif n == 3:
	partition = [2, 4, 4]
	permutations = remove_duplicates ( permute( partition ) )
elif n == 4:
	#partition = [4, 4, 4, 4]
	partition = [2, 4, 8, 8]
	permutations = remove_duplicates ( permute( partition ) )
	permutations.append( [4, 4, 4, 4] )
elif n == 5:
	partition = [2, 8, 8, 8, 8]
	permutations = remove_duplicates ( permute( partition ) )
	partition = [4, 4, 4, 8, 8]
	permutations += remove_duplicates ( permute( partition ) )		
elif n == 6:
	partition = [4, 4, 8, 8, 8, 8]
	permutations = remove_duplicates ( permute( partition ) )
elif n == 7:
	partition = [4, 8, 8, 8, 8, 8, 8]
	permutations = remove_duplicates ( permute( partition ) )
elif n == 8:
	#partition = [8, 8, 8, 8, 8, 8, 8, 8]
	permutations = [8, 8, 8, 8, 8, 8, 8, 8]
else:
	print "Número no válido."
		
print "Permutaciones:\n", permutations	

