# Your name: Ken Ma
# Your class-section: SECTION 1

weights = input("Enter grade weights: ").split() #put in the weights

avg = 0.0 #current grade average

# Complete the program!
# Do not change the supplied code
for i in weights: #loop weights for each one
    aaa = input("Enter grades ("+str(i)+"%): ").split() #enter in individual grades for each weight
    c = 0.0 #start at zero, similar format to avg
    for b in aaa: #loop individual grades in aaa list
        c += float(b) #sum of individual grades into c
    c = (c / len(aaa))*(float(i)/100) #product of average of individual grades and respective weight in decimal
    avg = avg + c #have current average added with weighted grade (loop)
print("Course grade:", round(avg)) #print out rounded, final course grade
