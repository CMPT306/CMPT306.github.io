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
#### Lab 3B - code2word
#### Due Sep 16, 2020, 9 AM

##### How Labs are Managed and Graded
1. Select a partner on your own. The rules are you must pair with a new partner each week.

2. Work as a pair to complete the lab. At the end of the lab period, make sure to share all files with each partner.

3. Each partner will submit the lab separately. (Submission instructions are described later in this lab.)

4. If you do not finish the lab during the lab period, you may either get together outside of class to complete it, or complete it on your own. If you choose to complete it on your own, be sure to indicate this in your submission.

5. Examples of cheating or collaboration can be found from this [link](http://cs.westminstercollege.edu/~jingsai/files/Cheating-or-Collaboration.html).
Stable Marriage Problem 

##### Instruction

This lab will involve writing python codes to find all possible English words combined by three IATA airport codes.

Please download and unpack this tar file:

- [lab3B.tar](./lab3B.tar)

which contains four files:

- airports_code.txt
- words_nine_letters.txt
- code2word_method1.py
- code2word_method2.py

An [IATA airport code](https://en.wikipedia.org/wiki/IATA_airport_code) is a three-letter code designating many airports around the world, defined by the International Air Transport Association (IATA). For example, BNA represents Nashville International Airport and SLC represents Salt Lake International Airport. There are 4445 codes, including all medium and large airports around the world, in file ***airports_code.txt***. 

You may wonder is it possible to find an English word which is combined by three airport codes (codes can be repeat)? The answer is yes! Here is an example, ABSTRACTS is combined by three codes: ABS (Abu Simbel Airport in Egypt), TRA (Tarama Airport in Japan), and CTS (New Chitose Airport in Japan). In this lab, your task is to find all such English words.

In order to simplify your task, you only need to search from 908 nine-letter long words taking from [10,000 most common English words](https://github.com/first20hours/google-10000-english). These words are saved in ***words_nine_letters.txt***.

A trivial solution to this lab is to enumerate all permutations of three codes with replacement from the pool of codes and then to check if the permutation is one of 908 words. However, via a mathematical estimation, you will find there are at least P(4445,3) = 87765155940 different possible combinations of three codes. If we compare each of this combination of codes with each word, the total number of comparisons is at least 87765155940\*908 = 79690761593520 $\approx$ 80 trillion. We need to find a better way to do it!

Instead of using permutation method, [Trie](https://en.wikipedia.org/wiki/Trie) is a wonderful data structure designed for solving this kind of problem. Basically, trie is a search tree - an ordered tree data structure which could be used to store a dictionary. Here is an example from [wiki](https://en.wikipedia.org/wiki/Trie).

<center>
<img src=./Trie_example.png width=300>
</center>

This is a trie for keys "A","to", "tea", "ted", "ten", "i", "in", and "inn". After building this trie using these keys, we can apply two basic methods: has_key() and has_subtrie():

- has_key(): Indicates whether a given key has value associated with this trie.

- has_subtrie(): Returns whether a given key is a prefix of another key in the trie.

For example, in this trie, these statements are true: has_key("ted"), has_key("inn"), has_key("in"), has_subtrie("i"), and has_subtrie("te"), while these statements are false: has_key("t"), has_key("te"), has_subtrie("to"), and has_subtrie("tea"). 

In this lab, you do not need to reinvent the wheel - trie. You can use this library: [pygtrie](https://github.com/google/pygtrie). Simply run "pip3 install pygtrie" or "pip install pygtrie" in the terminal to install it.  Starting with Python 3.4, pip command is included by default with the Python binary installers. But if you are a **Windows** user, you may need to add "%Path_to_python%\Scripts\" as a new path in the system environment before running pip in the terminal, where %Path_to_python% is the folder where you installed python. Please refer this [page](http://cs.westminstercollege.edu/~jingsai/courses/CMPT306/handouts/software/software.html) for finding the python path and adding path to global environment. 

Here is an example using pygtrie.

```python{.line-numbers}
import pygtrie as trie

codes = ["BN", "BNA", "SLC", "USA"]
# build a trie
t = trie.CharTrie()
for code in codes:
    t[code] = True

words = ["B", "BN", "BNA"]
# search words in this trie
for word in words:
    print("has_key(", word, "): ", t.has_key(word))
    print("has_subtrie(", word, "): ", t.has_subtrie(word))
```

Here are test results:
> has_key( B ):  False
has_subtrie( B ):  True
has_key( BN ):  True
has_subtrie( BN ):  True
has_key( BNA ):  True
has_subtrie( BNA ):  False

##### Two methods

Make sure you understand above example, code, and output before proceeding to next step. You are supposed to use both has_key() and has_subtrie() in this lab. 

We have two different ways solving this **code2word** problem. 

###### Method 1

We can use all *codes* to build a trie. In next step, we can break down a 9-letter long *word* into three successive 3-letter pieces. A word should be saved if all its three pieces are keys of the trie. The starting code of this method is **code2word_method1.py**. 

**hint**

Use [slice](https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/) of array, like `a[start:end], a[:end], a[start:]`.

###### Method 2

We also can use all *words* to build a trie. But in next step, we should search *codes* in this trie. The starting code of this method is **code2word_method2.py**. 

**hint**

Your code should run **less than 20 seconds**. 

##### What to Submit

You need to submit four files: **code2word_method1.py**, **results1.txt**, **code2word_method2.py**, and **results2.txt**. Please **do not** use other file names. Both lab partners need to submit the solution separately to the dropbox on Canvas.