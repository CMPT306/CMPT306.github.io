"""
Closest pair problem

This determines the closest pair of [x,y] points

"""

import random
import sys
import math

LOWER = -1000
UPPER = 1000

# return the distance between two parameters as Euclidean distance
def distance(a,b):
    pass

# populate the array with count unique random points
def populate(amount):
	a = []
	count = 0

	while count < amount:
		x = random.randint(LOWER,UPPER)
		y = random.randint(LOWER,UPPER)
		pair = (x,y)

		if pair not in a:
			a.append(pair)
			count += 1

	return a

""" 
now determine the closest pair
using brute force algorithm
"""
def closest(a):
    pass

    '''
    return as a dictionary
    i.e.
    return {'pt a': first point, 'pt b': second point}
    '''

def main():
	c = closest(populate(int(sys.argv[1])))
	
	# returned as a dictionary
	print 'point 1 = ', c['pt a']
	print 'point 2 = ', c['pt b']
	print 'closest = ', c['closest']

if __name__ == "__main__":
	main()
