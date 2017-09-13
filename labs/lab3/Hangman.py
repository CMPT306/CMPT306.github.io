'''
Hangman.py
'''

import sys
import random

class Hangman:
    '''
    Initializes the words list
    '''
    def __init__(self):
        file = open('words.txt','r')
        self.words = []
        self.wordguess = []
        for line in file:
            self.words.append(line.rstrip())

    '''
    Outputs the current status of the guesses
    '''
    def printword(self):
        for c in self.wordguess:
            print c,
        print

    def playgame(self):
        # generate random word
        word = self.words[random.randint(0,len(self.words)-1)]
        #print word
        self.wordguess = ['_'] * len(word)

        guesses = 0
        
        while guesses < 10:
            ch = raw_input('Enter a guess:').lower()
            
            ### Your code goes here:###

if __name__ == "__main__":

    game = Hangman()

    game.playgame()
