# Your name: Ken Ma
# Your class-section: SECTION1

# DO NOT CHANGE
import random
import math
import kmeans_viz
import kmeans_data

# TODO
# Returns a list (of length pigeons) in which
# each value is a valid and distinct number
# in the range [0, holes).
# When selecting each value, each should have an
# equal chance of being selected.
# Input: number of pigeons,
#        number of holes
# Output: list of length pigeons assigning
#         each pigeon to a hole
from random import randint #getting randint function from random module
def distinct_random_assignment(pigeons, holes): #function that takes in two variables to get result of whole number holes of # of pigeons
    result = [] #create empty list to house numbers in final result

    # == Follow these directions! ==
    # 1. Loop for each pigeon
    #    (a) Loop until done
    #        i.  Randomly select a value for the current pigeon
    #        ii. If it hasn't been previously assigned,
    #            add to the end of the result

    while len(result) != pigeons: #loop to keep going if length of result unequal to pigeons [length] remains true (until the two are equal)
        range1 = randint(0,holes-1) #have a random whole number less than holes into range1
        if range1 not in result: #only if range1 number is not in result list
            result.append(range1) #if so, then add number into the result list

    return result #output the result list (when length of result is equivalent to pigeons [length]; while ends)


# TODO
# Place a description here that succintly describes
# this function. Note how functions you wrote
# are used.
# Do NOT change code in this function!
# Input: describe inputs
# Output: describe outputs
def init_centroids(data, colors): #function that makes coordinate points from data [y] and colors [x] list (colors length) into another list
    k = len(colors) #have k be length of colors

    assignment = distinct_random_assignment(k, len(data)) #assignment being result of length of colors (k) and length of data in that function
    #the two lengths of variables used by distinct_random_assignment function

    initcentroids = [] #create empty list to store final output list
    for i in range(k): #loops as many times as the length of colors
        initcentroids.append([colors[i], data[assignment[i]]]) #combine colors and data (assignment) numbers into initcentroids list as coordinates

    return initcentroids #output the coordinates in list (numbers in list of list)


# TODO
# Compute the Euclidean distance
# between the supplied points
# Input: point1 point2 (assumed same length)
# Output: distance
from math import sqrt #get square root (sqrt) function from math module
def dist(p1, p2): #function to get the distance between to [coordinate] points
    # You MUST use at least one function
    # from the math module
    dist_long = 0 #distance of how long (dist_long) starting at zero
    for dist_i in range(len(p1)): #loops to go through each point(s) in list
        dist_long += float(((p1[dist_i]-p2[dist_i])**2)) #each point(s) goes through this part of the formula, adding them to the distance
    final_dist = sqrt(dist_long) #after all are added up, sqrt dist_long to get the actual euclidean distance
    return final_dist # your code here #outputs final euclidean distance from the calculations


# TODO
# Using a supplied distance function,
# find the index of the point in a dataset
# of options that is closest to a supplied point
# Input: point,
#        list of points,
#        distance function: df(p1, p2) -> #
# Output: index of closest option
def find_closest(p, options, df): #function to use a starting coordinate, surrounding coordinates, and previous function to get the closest point
    shorter = 0 #shortest distance at zero for the beginning, to know where to start
    count_range = 0 #count at zero, starting at zero index of list (first point)
    for position_i in range(len(options)): #loops through each point in options using its length
        closer = df(p,options[position_i]) #closer being the output of point (p) and that coordinate in inputted funcntion
        if shorter == 0: #only if shorter is zero; to know index is at zero
            shorter = closer #set shorter as closer, as it is the real shortest between two points so far
            closest_area = count_range #record index of the shortest (so far); the beginning
        else: #otherwise (shorter not being zero)
            if closer < shorter: #only if closer is smaller/shorter than shorter
                shorter = closer #set shorter as closer, as it is the shortest between two points so far (not beginning)
                closest_area = count_range #record index of the shortest (so far) after calculations
        count_range += 1 #add one to count_range as it goes through the index/indices of options [points]
    return closest_area # your code here #output the index of options point if it is the shortest between p (point)


# TODO
# Place a description here that succintly describes
# this function. Note how functions you wrote
# are used.
# Do NOT change code in this function!
# Input: describe inputs
# Output: describe outputs
def assign_to_closest(data, centroids): #function that takes in variables to bring closest of points
    k = len(centroids) #k as length of centroids

    assignment = [] #create empty list to store list for the final part
    options = [] #create empty list to hold the centroids
    for c in range(k): #loops through as many times as what k is (length of centroids)
        assignment.append([]) #have a list in a list for assignment
        options.append(centroids[c][1]) #puts certain numbers from centroids into options list (depends on index c)

    for p in data: #loops through the points in data list
        assignment[find_closest(p, options, dist)].append(p) #contains a list starting with the closest point x, y, data[x], and data[y]
        #might not work well with find_closest in between assignment and append

    return assignment #output assignment list (points/list in list)


# TODO
# Given a list of points,
# produce a point that is the dimension-wise
# average (i.e. dimension k is the average
# of all the dimension k values in the dataset)
# Input: dataset of points
# Output: list of average values
def avg_point(coordinates): #function that takes inputted coordinates to find the average point (avg_point)
    list_avg = [] #create empty list for the [final] average
    for pt_ind in range(0,len(coordinates[0])): #loops the numbers in points to go through each one
        sum = 0 #start of sum is zero; once it loops back, it will reset to zero to get avg of each
        for num_ind in range(0,len(coordinates)): #loops the point index/indices to go through each one
            sum += coordinates[num_ind][pt_ind] #add up the numbers in list(s) of that index
        avg_part = float(sum / len(coordinates)) #to get average, divide the added numbers by length of coordinates (# of lists in coordinates)
        list_avg.append(avg_part) #append/input the average into the list_avg list, so averages as many as # of indices of points
    return list_avg #output the list of averages


# TODO
# Place a description here that succintly describes
# this function. Note how functions you wrote
# are used.
# Do NOT change code in this function!
# Input: describe inputs
# Output: describe outputs
def update_centroids(centroids, assignment): #function that is trying to get numbers in centroids points changed to average of assignment points
    #returns none if there is no return part at the end
    for c in range(len(centroids)): #loops as many times as the length of centroids
        centroids[c][1] = avg_point(assignment[c]) #have the second number in points in centroids be the average point of numbers in lists in assignment
        #output none


# TODO
# Place a description here that succintly describes
# this function. Note how functions you wrote
# are used.
# Do NOT change code in this function!
# Input: describe inputs
# Output: describe outputs
#draws and inputs what points and instructions given to the function
def kmeans(data, colors): #function created that takes in two variables to get a kmeans picture using points
    kmeans_viz.title("Draw Data") #using this function to get a Draw Data title (window)
    for p in data: #loops through points in data
        kmeans_viz.draw_point("purple", p[0], p[1]) #when p in data, pointer will get a purple dot to that point
    kmeans_viz.wait() #have the pointer and function wait/pause

    kmeans_viz.title("Draw Initial Centroids") #using this function to get a Draw Initial Centroids title (window)
    centroids = init_centroids(data, colors) #centroids given points list using data and colors in init_centroids function
    kmeans_viz.draw_centroids(centroids) #draws certain points in the centroids using given variables
    kmeans_viz.wait() #have the pointer and function wait/pauses

    kmeans_viz.title("Draw Initial Assignment") #using this function to get a Draw Initial Assignment title (window)
    oldassignment = assign_to_closest(data, centroids) #using data & centroids, the function will figure out the points for oldassignment
    kmeans_viz.draw_assignment(centroids, oldassignment) #in lengths of centroids, function will draw points based on centroids & oldassignment
    #if it will work well with the assign_to_closest function

    kmeans_viz.title("Update Centroids") #using this function to get a Update Centroids title (window)
    update_centroids(centroids, oldassignment) #function trying to get numbers in centroids points changed based on average points from oldassignment
    kmeans_viz.draw_centroids(centroids) #draws certain points in the centroids using new points
    kmeans_viz.wait() #have the pointer and function wait/pause
    #none

    done = False #done equals to Boolean of False
    iteration = 1 #iteration is just one
    while not done: #loops while done is not False (until it is False)
        kmeans_viz.title("Iteration " + str(iteration)) #using this function to get a Iteration# depending on the iteration value title (window)
        newassignment = assign_to_closest(data, centroids) #have the function figure out the points using data and centroids for newassignment
        update_centroids(centroids, newassignment) #centroids points (numbers in points) to change with the averages using newassignment points
        #might not work perfectly

        kmeans_viz.clear() #reset screen with this function
        kmeans_viz.draw_centroids(centroids) #draw centroids points with given variable values
        kmeans_viz.draw_assignment(centroids, newassignment) #drawing of the points with given centroids and assignment coordinates

        done = (oldassignment == newassignment) #done equals to True/False of whether oldassignment matches with newassignment
        if not done: #to see if it is not done, so if it is True, then this proceeds
            oldassignment = newassignment #have oldassignment be newassignment value
            iteration += 1 #add one to iteration in this loop
            kmeans_viz.wait() #have the pointer and function wait/pause

    return centroids #outputs the centroids points


# DO NOT CHANGE
if __name__ == "__main__":

    random.seed(55513)
    kmeans_viz.setup(-60, -60, 60, 60, 0)

    centroids = kmeans(kmeans_data.SAMPLE, ["red", "blue", "black"])
    print(centroids)

    kmeans_viz.done()
