# DO NOT CHANGE
import statistics
import math
import string

# input: numeric value,
#        list of levels of precision (assumed to be natural numbers)
# output: string description including value at each level of precision
def precisions(val, digits):
    return [] # your code here!

# input: list-of-lists (sublists assumed equal length),
#        valid index
# output: list of values at supplied index
def values_at_index(l, i):
    return [] # your code here - MUST BE LIST COMPREHENSION!

# input: list-of-lists (sublists assumed equal length),
#        valid index
# output: (min, max, mean, stdev) of values at supplied index
def index_stats(l, i):
    return 0 # your code here!

# input: list-of-lists (sublists assumed equal length),
#        list-of-strings (assumed equal length to sublists of l),
# output: text summary of dataset
def quick_summary(l, dims, round_precision):
    return "" # your code here!

# input: list of words (any case),
#        list of bad words (any case),
#        what to replace bad words within in list of words
#        (if '', actually remove from list)
def censor(script, badwords, replace):
    script # your code here!, no return!

# input: single-character string,
#        whether y should count as a vowel
# output: if input is a vowel
#         relative to supplied counting of Y
def is_vowel(c, count_y):
    return False # your code here!

# input: word to convert (assumed lowercase)
# output: if first letter is a vowel add "way" to the end;
#         otherwise find the first vowel, move
#         beginning to end + "ay"
def pig_latin_word(s):
    return "" # your code here!

# input: string of space-separated words (no punctuation)
# output: string of space-separated pig-latin equivalents
def pig_latin_phrase(p):
    return "" # your code here!
