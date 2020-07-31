# Problem 1: Money Making Majors
# Name: Ken Ma

# Introduction: The data gathered here tells us majors, their starting salary
# and their final salary. The overall goal of this practicum is to import this data,
# clean the data, put it in a useful form to do calculations, and then display it

# It is an important issue to consider where your data is coming from: for sake of
# this example, you can assume the data is reasonable and ethical (though you should be careful about assuming that in the future)

# Instructions: Import the data from the majordata.txt file using the "open" function in python and play around with it
# Note that the data was entered in Europe, so they use commas in numbers where Americans would normally use periods
# That is, 24.12 (USA) = 24,12 (EUR)
# Your instructions are as follows:
# 1.) Import data from majordata.txt using the "open" function

# 2.) "Clean" the data and make it usable (you will need to get rid of that comma
# and change all numbers from strings to floating point)

# 3.) Find the percent change between starting and ending salary and store that information
# Reminder: percentChange = (ending-starting)/starting * 100

# 4.) Display what the maximum percent change is, along with the major that it corresponds to

# 5.) Display what the minimum percent change is, along with the major that it corresponds to

# 6.) Create a function that, when inputted with a number, returns all majors that have a
# percent change EXCEEDING the inputted value

# 7.) Use the statistics module to find the mean and standard deviation
# Display this data

# 8.) Create a function that, when inputted with a value, returns all data (displayed)
# that is at least that many standard deviations away from the mean
# Example: Mean = 2, std = 1: 4 is two standard deviations from the mean
# and 1/2 is 1.5 standard deviations from the mean

###################### Graded Part ##########################

# 9.) Build one last function where you input two values (call them a and b)
# and the function returns every percentage and its corresponding major, displayed nicely
# between a and b (including endpoints)

def emajor(text_file_path):
    majors_list = []
    for part_i in open(text_file_path, "r"):
        clean_majordata = ((part_i.replace(",",".")).strip()).split()
        #percentage_part = ((clean_majordata[2]-clean_majordata[1])/clean_majordata[1])*100
        majors_list.append(clean_majordata)
        #text_rows = [(file_rows.strip()).split() for file_rows in clean_majordata]
    print(majors_list)

#def inputv(a,b):

###################### Graded Part ##########################
