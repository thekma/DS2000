#Ken Ma
#SECTION1

# DO NOT CHANGE
import statistics
import math
import string

# input: numeric value,
#        list of levels of precision (assumed to be natural numbers)
# output: string description including value at each level of precision
def precisions(val, digits): #function that gets the decimal precisions with value and digits
    return [("Value with precision {} is {:."+str(d)+"f}.").format(d,val) for d in digits] #output a list of statements/string(s) of digits and values with digits number of decimals, from loop in digits

# input: list-of-lists (sublists assumed equal length),
#        valid index
# output: list of values at supplied index
def values_at_index(l, i): #function that generates a list of numbers from index in list of list
    return [x[i] for x in l] #output list that has number of each list in list (l) depending on the index (i) in loop

# input: list-of-lists (sublists assumed equal length),
#        valid index
# output: (min, max, mean, stdev) of values at supplied index
def index_stats(l, i): #function that makes index stats, so statistics with index from list
    part1 = values_at_index(l, i) #this part gets the numbers in list depending on index using values_at_index function
    min1 = min(part1) #obtains the minimum of the list of numbers in part1
    max1 = max(part1) #obtains the maximum of the list of numbers in part1
    mean1 = statistics.mean(part1) #obtains the mean/average of the list of numbers in part1
    stdev1 = statistics.stdev(part1) #obtains the standard deviation (stdev) of the list of numbers in part1
    return (min1, max1, mean1, stdev1) #output minimum, maximum, mean/avg, and stdev of the numbers in part1

# input: list-of-lists (sublists assumed equal length),
#        list-of-strings (assumed equal length to sublists of l),
# output: text summary of dataset
# dataset3 = [[0, 1, 2], [9, 8, 7], [3, 6, 12]]
def quick_summary(l, dims, round_precision): #function that makes a quick summary using min, max, mean, and stdev using the variables
    many_rows = len(l) #length of list is how many rows there are
    n_enter = 0 #how many times "\n" has been used to separate statements: zero
    starting1 = "Dataset has "+str(many_rows)+" rows"+"\n"+"Dimension analysis..."+"\n" #the starting/opening statement involving how many rows
    for x_i in range(len(dims)): #loop that has x_i go through the indices of dimensions to know the length of list; how many columns
        min1, max1, mean1, stdev1 = index_stats(l, x_i) #obtain min, max, mean, and stdev using index_stats function with list and index in list
        round1 = "{:."+str(round_precision)+"f}" #crucial part that will round the number(s) to a certain number of digits/precisions
        starting2 = " Dimension "+str(x_i)+" ("+str(dims[x_i])+"): min="+(round1).format(min1)+", max="+(round1).format(max1)+", mean="+(round1).format(mean1)+", stdev="+(round1).format(stdev1) #forms the whole end of statement with min, max, mean, and stdev with their rounding/precision
        starting1 += starting2 #add starting2 statement to the end of opening statement (starting1)
        n_enter += 1 #adds one to n_enter each time to know how many times statements have been produced
        if n_enter < len(dims): #to know if "\n" should be apply, without the last statement having "\n"
            starting1 += "\n" #add "\n" to end of statements, all except the last statement
    return starting1 #output the rows, and rounded: min, max, mean, and stdev using precision(s) in statements about dimension(s)

# input: list of words (any case),
#        list of bad words (any case),
#        what to replace bad words within in list of words
#        (if '', actually remove from list)
def censor(script, badwords, replace): #function that replaces badwords in script with replace replacements to censor them
    badwordsnew = [] #open up [new] empty list to store [script]
    [badwordsnew.append(bad_w.lower()) for bad_w in badwords] #has lowercase bad words entered into badwordsnew list in loop
    for script_word in script[:]: #loop that script word taken through in each script list; done so with slicing of list [:]
        script_test = script_word.lower() #have script test equal to lower case of script word to test script
        if script_test in badwordsnew: #test to see if script word is in badwordsnew list
            if replace == str(''): #afterwards, this is to see if replace variable is empty
                script.remove(script_word) #if so, have the badword(s) removed from script list
            else: #if none above, those if statements are not true
                script_i = script.index(script_word) #using index on script word to know the index in script list to figure out script index
                script[script_i] = str(replace) #using replace to have it in in the script list depending on its index in scipt list
    script #has script as final; no return function

# input: single-character string,
#        whether y should count as a vowel
# output: if input is a vowel
#         relative to supplied counting of Y
def is_vowel(c, count_y): #function that checks if 'c' letter is a vowel using count_y boolean
    all_vowels = ['a','e','i','o','u','y'] #all vowels listed out if count_y is True
    five_vowels = ['a','e','i','o','u'] #first five vowels listed if count_y is False
    if count_y == True: #to see if count_y is [equalivalent to] True to know which list to use
        if c in all_vowels: #afterwards, this is to see if that letter 'c' variable is a vowel in all_vowels
            is_bool = True #if so, is_bool takes in the True boolean
        else: #otherwise; 'c' variable letter is not in all_vowels
            is_bool = False #in that case, is_bool takes in the False boolean
    else: #otherwise; count_y is not True, so False, which determines the list to use
        if c in five_vowels: #afterwards, this is to see if that letter 'c' variable is a vowel in five_vowels
            is_bool = True #if so, is_bool takes in the True boolean
        else: #otherwise; 'c' variable letter is not in five_vowels
            is_bool = False #in that case, is_bool takes in the False boolean
    return is_bool #output True or False after is_bool is filled in with one of the boolean(s); True if letter is in list(s), False if not

# input: word to convert (assumed lowercase)
# output: if first letter is a vowel add "way" to the end;
#         otherwise find the first vowel, move
#         beginning to end + "ay"
def pig_latin_word(s): #function that can convert 's' word into pig latin word version
    a_vowel = False #a_vowel starts as False, as this will determine if letter in 's' word is a vowel
    latin_b = "" #start latin_b, latin back, with nothing to have it exist
    latin_f = "" #start latin_f, latin front, with nothing to have it exist
    if s[0] == 'y': #to see if the first letter of the word starts with 'y'
        for a_letter in s: #loop to go through each letter in 's' word
            if a_vowel == False: #to see if a_vowel is False
                a_vowel = is_vowel(a_letter,False) #if so, use is_vowel function with variables to figure out if the letter is a vowel
                if a_vowel == False: #if a_vowel is False, meaning the letter is not a vowel
                    latin_b += a_letter #if so, add letter to latin_b, pushing the letter to the back
            if a_vowel == True: #otherwise, if a_vowel is True, when letter is a vowel
                latin_f += a_letter #have the letter added to latin_f, starting the word with the vowel letter
    else: #otherwise, if the first letter is not 'y', any letter but 'y'
        for b_letter in s: #loop to go through each letter in 's' word
            if a_vowel == False: #to see if a_vowel is False
                a_vowel = is_vowel(b_letter,True) #if so, use is_vowel function with variables to figure out if the letter is a vowel
                if a_vowel == False: #if a_vowel is False, meaning the letter is not a vowel
                    latin_b += b_letter #if so, add letter to latin_b, pushing the letter to the back
            if a_vowel == True: #otherwise, if a_vowel is True, when letter is a vowel
                latin_f += b_letter #have the letter added to latin_f, starting the word with the vowel letter
    front_part = is_vowel(s[0],False) #use is_vowel function to know if the front part of 's' word starts with vowel letter, except 'y'
    if front_part == False: #to see if front part of word does not start with a vowel; front part is False
        pig_word = latin_f + latin_b + 'ay' #if so, have latin front at beginning combine with latin back with 'ay' at the end
    if front_part == True: #to see if front part of ward does start with a vowel; front part is True
        pig_word = latin_f + latin_b + 'way' #if so, have latin front at beginning combine with latin back with 'way' at the end
    return pig_word #output pig latin word that involves latin_f and latin_b and an 'ay' or 'way' part depending on the front of 's' word

# input: string of space-separated words (no punctuation)
# output: string of space-separated pig-latin equivalents
def pig_latin_phrase(p): #function that takes in 'p' phrase to have each word converted/transformed into pig latin [version]
    pig_phrase = "" #start pig_phrase, with nothing to have this [variable] exist/defined
    p_list = p.split() #this will have 'p' phrase turn into a list of strings for p_list
    p_len = len(p_list) #p_len is the length of p_list to know many list of strings there are
    for phrase_part in p_list: #loop that goes through each word/string (phrase_part) in p_list
        latin1 = pig_latin_word(phrase_part) #latin1 is phrase_part converted into pig latin using pig_latin_word function
        pig_phrase += latin1 #adds word-string (latin1) into pig_phrase
        if phrase_part != p_list[p_len-1]: #to see if the word/string is not the last in the phrase list
            pig_phrase += " " #if so, add a space in between the words in pig_phrase
    return pig_phrase #output 'p' phrase in pig latin text as pig_phrase
