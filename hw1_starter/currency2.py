# Your name: Ken Ma
# Your class-section: SECTION 1

# For the tests you should not change
# the contents of this list
# HOWEVER, your program should work
# no matter what the contents
# (i.e. we could change the number of
# currencies or which currencies are
# accepted)
accepted = ["USD", "RMB", "INR", "EUR"]

# Write your program here
# that uses the list above
c2in = input("Enter desired currency: ") #allows user to enter the currency code
c2out_s = int(len(accepted)) #figures out how many are in above list
c2out_e = c2in in accepted #looks in list to find the inputted currency code
print("Found in database (size="+str(c2out_s)+"):",c2out_e) #displays size of list and whether true or false
