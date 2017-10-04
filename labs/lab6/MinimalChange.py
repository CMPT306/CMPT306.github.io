'''
MinimalChange.py

Implementation of minimal change algorithm 
for generating permutations.

[ YOUR NAME GOES HERE]


Generates an *unordered* list of tuples containing 
permutations of the list of values.

For example, if values = [1,2,3]
this will return:
[ (1,2,3), (1,3,2), (3,1,2), (3,2,1), (2,3,1), (2,1,3) ]

'''

import sys

def permutate(value):

    pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Usage: python MinimalChange <size>'
        quit()

    result = permutate(int(sys.argv[1]))

    print result
