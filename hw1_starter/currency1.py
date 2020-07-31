# Your name: Ken Ma
# Your class-section: SECTION 1

# Your program!
c1in_d = int(input("Please enter number of US dollars: ")) #allows user to enter number of US dollars
c1in_c = float(input("1 USD = ? foreign: ")) #has user type in foreign rate
c1in_f = int(input("Fee for buying currency (in USD): ")) #requires user to input the fee
c1out = int((c1in_d-c1in_f)*c1in_c) #final calculations from US dollars to foreign currency
print("You have",c1out,"full unit(s) of foreign currency") #display final calculations
