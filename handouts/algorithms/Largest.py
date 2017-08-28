'''
Returns the largest element in list
'''
def largest(list):
    currentLargest = list[0]

    # Loops from position 1 to the end of the list 
    for element in list[1:]:
        if element > currentLargest:
            currentLargest = element


    return currentLargest
