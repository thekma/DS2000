# Your name: Ken Ma
# Your class-section: SECTION 1

# Your program!
mcin_phrase = input("Enter phrase: ") #input phrase by user
mcin_query = input("Enter query letters: ") #input letters whether in phase or query expected by user
count = 0 #counting of letters starts at zero
for a in mcin_phrase: #loop to go through each letter of phrase
    if a in mcin_query: #an if that looks for letter of phrase in query letters
        count = count + 1 #when letter of phrase is in query letters, add one to count
if count == 1: #after, if count is equal to one
    print("Phrase has "+str(count)+" letter in the query") #then output this statement with singular letter
else: #otherwise, when count not equal to one
    print("Phrase has "+str(count)+" letters in the query") #generate this statement with 'letters' (plural)
