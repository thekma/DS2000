#Ken Ma
#SECTION1

# TODO: returns the number of distinct letters in a word
# input: word
# output: number of distinct letters (case insensitive)
def num_distinct_letters(s): #function that gets the number of distinct letters in word, using s variable
    lower_word = s.lower() #lower() method turns all letters in word to lower case, as upper case is different from lower case
    letters_differ = [] #opens empty list to collect any letters that differ from each other
    [letters_differ.append(letter_i) for letter_i in lower_word if letter_i not in letters_differ] #comprehension going through each letter in list, append into letters_differ if new letter not in the list
    distinct_len = len(letters_differ) #len to get the number of distinct letters in the letters_differ list
    return distinct_len #output number of distinct letters in the word; including case insensitive

# TODO: tests if the word contains q but not qu
# input: word
# output: 1 if the word contains q, but not qu (case insensitive),
#         0 otherwise
def q_not_qu(s): #function checks if word has any 'q' letter(s) to give 1 score but if it has 'qu' letters then 0 score regardless of 'q'
    lower_case = s.lower() #lower() method turns all letters in word to lower case, as upper case is different from lower case
    current_score = 0 #score starts at zero, just so if there aren't any 'q' letter(s) [to get one] including 'qu' (which still gives zero)
    for letter_ii in lower_case: #loop that goes through each letter in lower case version of word from s variable
        if letter_ii == 'q': #to see if the letter is 'q' as it goes through the loop
            current_score = 1 #if the letter is 'q' then the score is one
    if 'qu' in lower_case: #to see if 'qu' letters exist in the lower case of word
        current_score = 0 #if 'qu' is in lower_case then zero is the score, overriding previous one(s)
    return current_score #output the score of the word, either zero or one

# TODO: scores a letter based upon a scoring scheme
# input: single letter,
#        sequence of pairs: ('letter', score),
#        default score if letter is not in pairs
# output: if the letter (case insensitive) is in the pairs then that score,
#         otherwise the default score
def letter_score(letter, letter_scores, default_score): #function obtains score of the letter, whether from letter_scores or default_score
    letter_upper = letter.upper() #upper() method to turn letter into upper case; works if there is an upper case of letter in letter_scores
    letter_lower = letter.lower() #lower() method to turn letter into lower case; works if there is a lower case of letter in letter_scores
    score_board = default_score #scoreboard at zero, just so if letter in lower or upper case doesn't match letters in letter_scores
    for score_i in range(len(letter_scores)): #loop that has score_i go through indices of letter_scores
        score_letter = letter_scores[score_i][0] #score_letter is a letter in letter_scores; each letter for each iteration
        if letter_upper == score_letter: #to see if upper case of letter matches with this letter in letter_scores
            score_board = letter_scores[score_i][1] #if so then the scoreboard will be the score next to the letter in letter_scores
        if letter_lower == score_letter: #to see if lower case of letter matches with this letter in letter_scores
            score_board = letter_scores[score_i][1] #if so then the scoreboard will be the score next to the letter in letter_scores
    return score_board #output the score/scoreboard of the letter; score from either letter_scores or just default_score

# TODO: compute a word score based upon letter-score pairs and a default score
# input: word of letters,
#        sequence of pairs: ('letter', score),
#        default score if a letter is not in pairs
# output: the sum of the scores of each letter (case insensitive)
def word_score(word, letter_scores, default_score): #function sums overall score, going through each letter for score
    score_sum = 0 #score as a sum is nothing so far, which is why zero, but score_sum won't stay as this zero
    for word_letter in word: #loop that has word_letter go through each letter in word
        score_part = letter_score(word_letter, letter_scores, default_score) #score_part made from using the letter_score function with three variables given
        score_sum += score_part #score_sum to add-on score_part
    return score_sum #output score_sum (total score) after going through each letter in word (adding corresponding scores)

# DO NOT CHANGE
def scrabble_score(word):
    SCRABBLE = (
        ('D', 2), ('G', 2),
        ('B', 3), ('C', 3), ('M', 3), ('P', 3),
        ('F', 4), ('H', 4), ('V', 4), ('W', 4), ('Y', 4),
        ('K', 5),
        ('J', 8), ('X', 8),
        ('Q', 10), ('Z', 10)
    )

    SCRABBLE_DEFAULT = 1

    return word_score(word, SCRABBLE, SCRABBLE_DEFAULT)


# DO NOT CHANGE
def length_score(word):
    return word_score(word, (), 1)


# TODO: find all the words in a file that have the highest "score"
#       according to a function
# input: path to a file of words,
#        function by which to score each word
# output: (highest score, [all words in the file that have the highest score])
#         words should appear in the list in the same order as in the file
def most_words(file_path, measure_func): #function gets the maximum score and its respective word(s), (from file, using function to measure)
    with open(file_path, 'r') as new_file_path: #opens file in file_path, having it as read, naming file as new_file_path for this function
        max_list = [] #open up empty list to store numerical values
        data_list = [] #open up empty list to store word values
        for word_value in new_file_path: #loop that has word_value go through each word or value in the file
            word_value = word_value.strip() #strip() method used to clear empty spaces before, after, or outside of the line of values/words
            data_value = measure_func(word_value) #data_value made from using an inputted function with word_value as the variable
            data_list.append(word_value) #word_value appended into data_list [list]
            max_list.append(data_value) #data_value appended into max_list [list]
        max_value = max(max_list) #max_value to be the maximum value from max_list
        words_list = [] #open up empty list to store words that correspond with max_value
        for value_part in range(len(max_list)): #loop that has value_part go through indices of max_list
            if max_list[value_part] == max_value: #to see if max_list value of value_part index equals to max_value
                max_word = data_list[value_part] #if so then have max_word be data_list value of same index using value_part
                words_list.append(max_word) #max_word appended into words_list
    return max_value, words_list #output max_value (maximum value) and words_list (list of words corresponding to max_value)

# TODO: read a file of whitespace-separated data with a header row
# input: file path
# output: (['header names'], [[rows],])
def read_data(file_path): #function displays the header and the lines of rows afterwards, using file in file_path
    with open(file_path, 'r') as read_path: #opens file in file_path, having it as read, naming file as read_path for this function
        header = ((read_path.readline()).strip()).split() #header to be the first line of read_path [file]; cleaned up with strip() and split() to clear empty spaces and have values in list
        data_rows = [(file_row.strip()).split() for file_row in read_path] #data_rows to be the line(s) after header as it has file_row loop through each line in file; cleaned up with strip() and split() to clear empty spaces and have values in list
    return (header, data_rows) #output header list and data_rows lists [in parentheses]

# TODO: get a column of data based upon column name
# input: column name,
#        row of column names,
#        list-of-lists of data
# output: values from all rows of data in the column
#         identified by the supplied name (in the
#         order the rows appear)
def get_column(name, header, data): #function to get column of values/numbers that corresponds to name in header (same index)
    name_index = header.index(name) #name_index to be index of name in header
    return [data[data_i][name_index] for data_i in range(len(data))] #output values/numbers from data of that index (name_index) as data_i loops through indices of data

# TODO: given a column of '#', convert to #
# input: list of string representations of numbers,
#        precision to round output values
# output: list of rounded numbers
def convert_to_nums(l, round_precision): #function converts l number value(s) to be number value(s) with decimals as many as round_precision
    return [round(float(l_num),round_precision) for l_num in l] #output numbers rounded to round_precision (# of decimals) as l_num loops through each number value in l [list]

# TODO: get all the data about player with highest rating
# input: file path
# output: row of data from the file for the player
#         with the highest rating
def player_with_highest_rating(file_path): #function extracts a player row in file based on highest rating
    with open(file_path, 'r') as player_rate_path: #opens file in file_path, having it as read, naming file as player_rate_path for this function
        open_max = [] #open up empty list to store player ratings
        players_list = (read_data(file_path))[1] #players_list to be [players] rows/lines after header, using read_data function
        for player_i in players_list: #loop that has player_i go through each player row/line in players_list
            open_max.append(player_i[10]) #rating of player_i player appended into open_max list
            open_nums = convert_to_nums(open_max,1) #open_nums to be number of open_max rounded to one decimal, using convert_to_nums function
            max_num = max(open_nums) #max_num to be the maximum value of open_nums
            if float(player_i[10]) == max_num: #to see if rating of player_i player equals to max_num value
                max_index = players_list.index(player_i) #if so then max_index equals to the index of this player_i in players_list
    return players_list[max_index] #output player row/line (max_index [index] of players_list), based on highest rating

# TODO: given a column of '#%', convert to #
# input: list of string representations of percentages,
#        precision to round output values
# output: list of rounded proportions
def convert_to_props(l, round_precision): #function converts percentages in l to decimals, using round_precision as number of decimals
    decimal_list = [] #open up empty list to store the decimal points
    for percent_num in l: #loop that has percent_num go through each percentage in l
        base_num = percent_num.replace("%","") #base_num to be percent_num without its '%' sign
        decimal_pt = round((float(base_num) / 100),round_precision) #decimal_pt to be base_num divided by a hundred, rounded with round_precision, to get decimal version
        decimal_list.append(decimal_pt) #decimal_pt appended into decimal_list
    return decimal_list #output decimal_list (decimals converted from percentages) [list]

# TODO: get the first and last names of all players with under 60% completion
# input: file path
# output: [['first', 'last'],]
def player_names_with_bad_completion(file_path): #function lists players (first & last names) with completion % less than 60% (0.6)
    with open(file_path, 'r') as bad_path: #opens file in file_path, having it as read, naming file as bad_path for this function
        percent_list = [] #open up empty list to store percentages that players have
        names_list = (read_data(file_path))[1] #names_list to be rows after header
        [percent_list.append(name_i[9]) for name_i in names_list] #percentages that players have appended into percent_list as name_i loops each row in names_list
        player_decimals = convert_to_props(percent_list,3) #player_decimals to be decimals of three decimal points, using convert_to_props
        bad_list = [] #open up empty list to store indices
        [bad_list.append(player_decimals.index(decimal_i)) for decimal_i in player_decimals if decimal_i < 0.6] #decimal_i indices to be appended into bad_list if decimal_i less than 0.6 as decimal_i loops through each decimal in player_decimals
        bad_player_name = [] #open up empty list to store player names
        for bad_index in bad_list: #loop that has bad_index go through each index of players with less than 0.6 (bad_list)
            player_name = [str(names_list[bad_index][0]), str(names_list[bad_index][1])] #player_name to be first and last names of player, corresponding to bad_index
            bad_player_name.append(player_name) #player_name appended into bad_player_name [list]
    return bad_player_name #output lists of player names with below 60% completion (bad_player_name)

# TODO: query a field for a row that matches a field/value pair
#       (assumes only a single row has the if_field/if_value pair)
# input: field for which to get the value,
#        field to check,
#        value to check in the field,
#        path to file
# output: value of the queried field in the row that
#         matches the if_field=if_value pair
def query_field_if(q_field, if_field, if_value, file_path): #function displays value under q_field and same row as if_value in file (file_path)
    with open(file_path, 'r') as query_path: #opens file in file_path, having it as read, naming file as query_path for this function
        query_titles = (read_data(file_path))[0] #query_titles to be header of the file
        query_lists = (read_data(file_path))[1] #query_lists to be rows/lines after header
        if_column = get_column(if_field,query_titles,query_lists) #if_column to be column of numbers (values with same index) under if_field, using get_column function
        q_column = get_column(q_field,query_titles,query_lists) #q_column to be column of numbers (values with same index) under q_field, using get_column function
        for column_v in if_column: #loop that has column_v go through the numbers in if_column
            if column_v == if_value: #to see if column_v of if_column equals to if_value, to know the row, as it goes through each iteration
                if_row = if_column.index(column_v) #if so then if_row is column_v index of if_column
        q_value = str(q_column[if_row]) #q_value to be the value under q_field in if_row (index in q_column)
    return q_value #output value under q_field that has row/line matching with if_value, showing q_value
