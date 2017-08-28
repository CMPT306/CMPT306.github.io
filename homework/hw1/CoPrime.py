'''
    CoPrime.py

    Generates a graph of the m x n co-primes
    
    [YOUR NAME GOES HERE]
'''

import sys

'''
generates the co-primes in an m x n matrix
'''
def coprimes(m, n):
    '''
    creates a list of size n each with
    each element initialized to None
    '''
    result = [None] * (m + 1)

    '''
    each element in the list is now a
    list of size m where each value
    is initialized to a space ' '
    '''
    for i in range(0,m+1):
        result[i] = ['^'] * (n + 1)
        
    '''
    output the contents of result
    '''
    for x in result:
        # x[:] is a list "slice"
        for y in x[:]:
            '''
            by putting a comma at the end, we prevent a newline
            '''
            print y,
            
        print

    '''
        YOUR WORK WILL GO HERE
    '''


# behaves like main() method

if __name__ == "__main__":
    # some error checking
    if len(sys.argv) != 3:
        print 'Usage\n python CoPrime [int] [int]'
        quit()

    coprimes(int(sys.argv[1]), int(sys.argv[2]))
