# Your name: Ken Ma
# Your class-section: SECTION 1

# Returns the absolute value
# of the supplied value
# Input: number
# Output: number
def myabs(a): #function that gets absolute value of 'a'
    if a > 0: #'a' greater than zero
        return a #normal value (unchanged)
    else: #not 'a' greater (less than zero)
        return -a #negative value of 'a'

# Returns the taxi-cab distance
# between the supplied list of coordinates
# Input: two lists of numbers (assumed same length)

# Output: number
def mymanhattan(p1, p2): #function that generates the manhattan distance of two points
    mym_dist = 0 #final manhattan distance start at zero
    for i in range(len(p1)): #loop to get how many numbers in manhattan point(s)
        mym_point = abs(p1[i]-p2[i]) #part that has numbers go through subtraction then absolute value
        mym_dist += mym_point #add that part of calculations into the final distance
    return mym_dist #output final distance after going through each numbers within points

# Returns the number of positions that have
# different values in the supplied
# list of coordinates
# Input: two lists of numbers (assumed same length)
# Output: number
def myhamming(p1, p2): #function that makes the hamming distance of two points
    myh_count = 0 #final hamming count start at zero
    for i in range(len(p1)): #loop to get how many numbers in hamming point(s)
        if p1[i] != p2[i]: #to see if first point number is different from second point number
            myh_count += 1 #if so, add one onto final count
    return myh_count #output final count after comparing each numbers in the points

# Returns the straight-line distance
# between the supplied list of coordinates
# Input: two lists of numbers (assumed same length)
# Output: number
def myeuclidean(p1, p2): #function that creates the euclidean distance of two points
    mye_d = 0 #euclidean distance part start at zero
    for i in range(len(p1)): #loop to get how many numbers in euclidean point(s)
        distance2 = ((p1[i]-p2[i])**2) #piece of euclidean formula that calculates by subtraction then exponentiation
        mye_d += distance2 #sum up the calculated distance with the distance part
    euclidean_d = (mye_d)**(0.5) #the final part needed is square root of all that summed up in distance part
    return euclidean_d #output euclidean distance as the final calculations of the points (euclidean)

# Returns the label of the item in the
# "community" that is closest
# to the search point ("p") according
# to the distance function ("df")
# Input:
#   p = [coordinates]
#   community = [["label", [coordinates]],]
#   df = function([coordinates], [coordinates]) -> number
def nearestneighbor(p, community, df): #function that takes in variables to have the nearest neighbor
    short = 0 #shortest distance start at zero
    for ii in range(len(community)): #loop to get how many numbers/lists within community
        dist = df(p, community[ii][1]) #df function calculates the distance between current point and community point to get THAT DISTANCE
        if short == 0: #at the start, shortest is zero, to have it go through as the process, being replaced (check if zero)
            short = dist #have shortest (0) change to THAT DISTANCE (new distance), as zero is a starter, not an actual distance between points
            name1 = community[ii][0] #THAT DISTANCE is the true shortest for now, so have the community point label as the name (name1)
        else: #shortest distance (currently) is not zero
            if dist < short: #check if THAT DISTANCE (new) is less than the shortest distance (currently)
                short = dist #if so, change THAT DISTANCE as the new shortest
                name1 = community[ii][0] #THAT DISTANCE is the shortest for now, so have the community point label as the name (name1)
    return name1 #output the final nearest neighbor label of the community point(s) after calculating the shortest distance
