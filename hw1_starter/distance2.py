# Your name: Ken Ma
# Your class-section: SECTION 1

# Your program!
d2in = int(input("Please enter full number of inches: ")) #allows user to enter number of inches
d2out_y = int(float(d2in//36)) #gets yards from inches
d2out_f = int((d2in%36)//12) #remainder of yards in feet
d2out_i = int((d2in%36)%12) #remainding inches
print(str(d2in)+"in =",str(d2out_y)+"yd",str(d2out_f)+"ft",str(d2out_i)+"in") #full, extended measurements of inches
