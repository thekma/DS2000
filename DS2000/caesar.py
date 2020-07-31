# Problem 2: Caesar Shift
# Name:

# Introduction: A Caesar Shift is a type of code. Essentially, we generally think of
# A = 1 --> A, B = 2 --> B, C = 3 --> C, D = 4 --> D, E = 5 --> E, F = 6 --> F, G = 7 --> G, H = 8 --> H, I = 9 --> I, J = 10 --> J .... Z = 26 --> Z
# However, sometimes we want to shift this. That is to say, if we shift by 5, our numbers become
# A = 6 --> F, B = 7 --> G, C = 8 --> H, D = 9 --> I, E = 10 --> J, F = 11 --> K, G = 12 --> L, H = 13 --> M, I = 14 --> N, J = 15 --> O .... Z = 5 --> E
# So the message DAB --> 4,1,2 --> 9,6,7 --> IFG

# Website: https://en.wikipedia.org/wiki/Caesar_cipher

# Instructions 1: Build a function (call it julius(word,shift))
# that, when inputted with some word as a string and some shift, returns
# the coded word, using a Caesar Shift of that amount

# You can assume that your word is given in lower case letters
# but you should think about how you would adjust your code to be more general

# Instructions 2: A quick way to decode Caesar shift is to check every single
# possible shift and see if any of those are a word you would recognize.
# First do this using a standard "for" loop, and then do it....
# ....using LIST COMPREHENSION, build a function (call it nero(codedMessage,listOfWords))
# that generates that a list of all possible words using Caesar shift,
# compares it to list of possible words (listOfWords) below,
# and tells you what the shift is as a result.

listOfWords = ['augustus','claudius','tiberius','titus','marcusaurelius','commodus','maximinusthrax','friend','herald', 'performance','northeastern','samuel','judge','practicum','ccis', 'python', 'practically', 'amazing', 'picture','warrenbuffet','billgates','wilbur','babe']

# Decode the following words, using this list of words, and find the corresponding shift.
# Word 1: wyhjapjbt
# Word 2: fgjlzwsklwjf
# Word 3: nbsdvtbvsfmjvt
# Word 4: tnznlmnl

# Challenge Question #1: Extend your code to work for a string/message of any length
# Hint: The hard part of this is going to be figuring out what to do with spaces

# Challenge Question #2: Build a function (call it brutus(codedMessage,shift))
# that, when inputted with some string of coded message and some shift, returns
# what the original message was. In short, make a function that undoes julius


# Example: julius('samuel',12) = 'emygqx'
# Example: julius('judge',22) = 'fqzca'
# Example: julius('supercalifragilisticexpialidocious',10) = 'cezobmkvspbkqsvscdsmohzskvsnymsyec'
# Example: julius('herald',26) = 'herald'

# Example: nero('emygqx',listOfWords) = ('samuel', 12)
# Example: nero('fqzca',listOfWords) = ('judge', 22)

# Example: brutus('emygqx',12) = 'samuel'
# Example: brutus('cezobmkvspbkqsvscdsmohzskvsnymsyec',10) = 'supercalifragilisticexpialidocious'

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vowels = ['a','e','i','o','u','y']

def shifting(oneword,onenumber):
    for i in oneword:
        letter_i = (alpha.index(i)) % 26
        letter_shift = letter_i + onenumber
        newletter = alpha[letter_shift]
        word_new += newletter
    return word_new
