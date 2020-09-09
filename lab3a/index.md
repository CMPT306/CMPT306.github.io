---
export_on_save:
  html: true
html:
  toc: true
  offline: true
---

### CMPT 306 Algorithms and Data Structures
#### Fall 2020
---
#### Lab 3A - Hangman
#### Due Sep 16, 2020, 9 AM

##### How Labs are Managed and Graded
1. Select a partner on your own. The rules are you must pair with a new partner each week.

2. Work as a pair to complete the lab. At the end of the lab period, make sure to share all files with each partner.

3. Each partner will submit the lab separately. (Submission instructions are described later in this lab.)

4. If you do not finish the lab during the lab period, you may either get together outside of class to complete it, or complete it on your own. If you choose to complete it on your own, be sure to indicate this in your submission.

5. Examples of cheating or collaboration can be found from this [link](http://cs.westminstercollege.edu/~jingsai/files/Cheating-or-Collaboration.html).
Stable Marriage Problem

This lab will involve writing a solution to the classic game of Hangman where players get 10 guesses to guess a word chosen by random from your game.

##### Overview

The following file contains a Python script that is passed  file containing the words to be chosen from ([words.txt](./words.txt))

##### Starting code

- [lab3A.tar](./lab3A.tar)

##### The Game

The game can be written in any style that you choose. The important thing is that you account for the following:

- <span style="color:red"> Use a lambda expression and map at least once somewhere in your code. </span> You can use this [page](https://www.python-course.eu/lambda.php) as reference. 

- Only 10 times guesses are allowed.

- Only allow alphabetic characters to be considered. If a user enters a *, skip over the input. (Python has a pretty useful function to check if a string is alphabetic.). In this case, print "Only allow alphabetic characters." Do not count this input.

- If a user input empty or more than one characters in one input like 'as', do not consider this kind of input and do not count this input. In this case, print "Only one character is allowed in each input".

- The file you are choosing words from (words.txt) contains all lower-case characters. You can allow a user to enter an upper-case alphabetic character (A .. Z), but get its lower-case equivalent when comparing.

- If a user enters a character that appears more than once in the word (i.e. 'aardvark' where 'a' occurs multiple times) be sure to identify each occurrence of the character, and not just the first.

- Allow a user to guess a character only once. If they enter the same character more than once, print out a message indicating the character has already been considered and only count the same character once. Furthermore, if the character is an incorrect guess, only count it as an incorrect guess the first time. In this case, print "The letter", ch, "has already been used."

- If a user enters a character that is not in the correct word, print ch,"does not occur."

- If scuess, print 'Congratulations!', otherwise, print 'Sorry dude, the word is', word

- Print the current times of count along with each output. 

##### Lambda expression

* Use as an anonymous function 

```python {.line-numbers}
# addfile is a lambda function with one argument
addfive = lambda x: x +5
# output is 10
print(addfive(5))

# add is a lambda function with two arguments
add = lambda x,y: x +y
# output is 11
print(add(5,6))

# isA is a lambda fuction using if-else
isA = lambda x: True if x == 'A' else False
# output is False
print(isA('b'))
# output is True
print(isA('A'))

```

* Use with map or filter

```python{.line-numbers}
mylist1 = [1,2,3]
# double each element in mylist 
lista = list(map(lambda x: x*2, mylist))
# output is 2,4,6
print(lista)

mylist2 = [4,5,6]
# element-wise addition between two lists
listb = list(map(lambda x,y: x+y, mylist1, mylist2))
# output is 5,7,9
print(listb)
```

##### What to Submit

Be sure to include your names at the top of each source file. Refer to program grading guidelines for best practices for submitting source code.

Please submit your code to Canvas. Be sure to include the names of each partner on the submission. 

Please do not use other file names. Both lab partners need to submit the solution separately to the dropbox on Canvas
