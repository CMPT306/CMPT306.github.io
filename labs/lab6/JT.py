'''
Implementation of Johnson Trotter algorithm 
for generating permutations.

[ YOUR NAME GOES HERE]


Generates an unordered list of tuples containing 
permutations of the list of values.

For example, if values = [1,2,3]
this will return:
[ (1,2,3), (1,3,2), (3,1,2), (3,2,1), (2,3,1), (2,1,3) ]

'''

import sys

def permutate(values):
    result = [ ]
    
    latestPermutation = [v for v in values]
    
    print latestPermutation

    '''
    Initialize each value to a left-arrow
    '''
    mappings = { }
    
    for v in values:
        mappings[v] = False
   
    '''
    tuplify the latest permutation
    ''' 
    result.append(tuple(latestPermutation))
    
    return result

'''
reverses the direction of all elements in the perms list
that are larger than k
'''
def reverseDirection(mappings, perms,k):
    for v in perms:
        if v > k:
            if mappings[v] == True:
                mappings[v] = False
            else:
                mappings[v] = True


'''
Determines if an element at position i
in the perms list is mobile

Value of False is left arrow
Value of True is right arrow
'''
def isMobile(mappings, perms, i):
    if (mappings[perms[i]] == False):
        # look to the left
        if i > 0 and (perms[i] > perms[i-1]):
            return True
        else:
            return False
    else: 
        # look to the right
        if i < len(perms) - 1 and perms[i] > perms[i+1]:
            return True
        else:
            return  False 


'''
Find the largest mobile element
'''
def findLargestMobileElement(mappings, perms):
    largest = float("-inf")
    largestIndex = 0
    
    for i in range(0,len(perms)):
        if isMobile(mappings,perms,i):
            if perms[i] > largest:
                largest = perms[i]
                largestIndex = i
                
    return (largest, largestIndex)
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Usage: python JT <size>'
        quit()

    startingList = [(i + 1) for i in xrange(int(sys.argv[1]))]
    
    result = permutate(startingList)
    
    print result
