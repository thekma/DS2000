# Your name: Ken Ma
# Your class-section: SECTION 1

# Do not change this in any way!
brackets = [
    ["single", 12000, 0.37,
        [[     0,   9525, 0.10],
         [  9526,  38700, 0.12],
         [ 38701,  82500, 0.22],
         [ 82501, 157500, 0.24],
         [157501, 200000, 0.32],
         [200001, 500000, 0.35]]],
    ["married", 24000, 0.37,
        [[     0,  19050, 0.10],
         [ 19051,  77400, 0.12],
         [ 77401, 165000, 0.22],
         [165001, 315000, 0.24],
         [315001, 400000, 0.32],
         [400001, 600000, 0.35]]]
]

income = round(float(input("Enter income: ")))
status = input("Enter filing status: ")

# Complete the program!

# This code below is to help you get started,
# feel free to change as you see fit!

bi = 0 # desired bracket index (set this based upon entered status)
new = 0 #start at zero for deducted income
for b in range(len(brackets)): # for all filing statuses
    #print(b, brackets[b][0]) # print bracket index and its status
    if status == brackets[b][0]: #sees if status matches with one of two brackets
        new = income - brackets[b][1] #new is deducted income depending on status
        bi = b #bracket index has a specific bracket
#print(brackets[bi][1]) # print standard deduction of desired bracket index

finalpt = brackets[bi][3][5][1] #finalpt is end point (500k single or 600k married)
#print("finalpt:",brackets[bi][3][5][1])
finalrate = brackets[b][2] #finalrate is 0.37, single or married (depending)

store = 0 #for storing parts of tax calculated, currently at zero
for bracket in brackets[bi][3]: # loop over all levels in the desired bracket index
#    print(bracket[0], bracket[1], bracket[2]) # print lower/upper amounts, and tax rate
    #print("eachbracket:",bracket[1])
    if new > bracket[1]: #checks if deducted income is higher than max of bracket
        #print("n>b b1:",bracket[1])
        #print("n>b b0:",bracket[0])
        #print("n>b b2:",bracket[2])
        if bracket[0] == 0: #checks if first bracket, very beginning equals zero
            store = store + ((bracket[1]-bracket[0])*bracket[2]) #calculates and stores into store
            #print(".................................(b1-b0)*b2:",store)
        if bracket[0] > 0: #checks if min/start of bracket is greater than zero
            #print("b>0 b0:",bracket[1])
            #print("b>0 new:",new)
            if bracket[1] == finalpt: #checks if max of bracket equals finalpt (500k or 600k)
                #print("bracketsbi2:",bracket[2])
                store = store + ((bracket[1]-(bracket[0]-1))*bracket[2]) #if so, calculate and add to store
                #print(".................................(b1-b0)*b2***:",int((bracket[1]-(bracket[0]-1))*bracket[2]))
                #print("collective:",store)
                store = store + ((new-bracket[1])*finalrate) #then, finish with final calculation with final rate into store
                #print(".................................(new-b1)*finalrate:",int((new-bracket[1])*finalrate))
                bi = round(finalrate*100) #update bi to latest decimal of bracket
            else: #if max does not equal finalpt then this happens
                store = store + ((bracket[1]-(bracket[0]-1))*bracket[2]) #only calculate and add to store
                #print(".................................(b1-b0)*b2:",int((bracket[1]-(bracket[0]-1))*bracket[2]))
                bi = round((bracket[2])*100) #update bi to latest decimal of bracket
    if bracket[1] > new > bracket[0]: #checks if max of bracket is higher than deducted income; new > min
        store = store + ((new-(bracket[0]-1))*bracket[2]) #calculate and add to store
        #print("b>n bracket1:",bracket[1])
        #print("new:",new)
        #print("bracket0:",bracket[0])
        #print(".................................(new-b0)*b2:",int((new-(bracket[0]-1))*bracket[2]))
        #print("laststore:",store)
        bi = round((bracket[2])*100) #update bi to latest decimal of bracket
        #print("bi:",bi)

effectiverate = round((round(store)/income)*100) #calculates effective rate; rounds it
totalstore = round(store) #rounding the total store calculations
if totalstore > 0: #determines if total is greater than zero
    print("You are in the "+str(bi)+"% bracket; you owe $"+str(totalstore)+" in taxes for an effective rate of "+str(effectiverate)+"%.") #output this if greater
else: #if not greater than zero
    print("You do not owe any taxes!") #output no taxes
