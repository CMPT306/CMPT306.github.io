
# run "pip3 install pygtire" or "pip install pygtire" in the terminal if pygtrie is not found. 
import pygtrie as trie  

# read codes of airport
codes = []
path_to_code_file = 'airports_code.txt'
with open(path_to_code_file, 'r') as f:
    codes = f.read().splitlines()

# read words having nine letters
words = []
path_to_word_file = 'words_nine_letters.txt'
with open(path_to_word_file, 'r') as f:
    words = f.read().splitlines()

# build a trie using words
t = trie.CharTrie()
for word in words:
    t[word] = True

# search codes from the trie
results2 = [] # append words, which is a combination of three codes, to results. 
# Your code goes here:





## write results into results.txt
with open('results2.txt', 'w') as file_handler:
    for word in results2:
        file_handler.write("{}\n".format(word)) 