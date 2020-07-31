# Problem 4: Circle
# Name:

# Introduction: We are going to use the random module to play around with circles
# Overall, the goal will be to generate a random point (x,y), and determine if it is in
# the circle of radius 1 centered at (0,0)
# You do this by finding if the Euclidean distance between your point and (0,0)
# are within 1 of each other
# Use the random module and the uniform function in there
# uniform(a,b) function will randomly select a number between [a,b], including 0 but not including 1

# Instructions: You should build two functions, one that measure the Euclidean distance
# between two points, p1 and p2 (you can assume that p1/p2 are lists of two elements)
# The second function will input n, and you will randomly generate n points (x,y) using random
# function, and then will check if that point is in the circle of radius 1
# Your function will keep track of all the times the point is in the circle out of n,
# and will return the ratio of that to (2*n). (i.e. # number of times the point is in the circle / (2*n)

# Extra Challenge: You can use this to approximate pi. :) Can you figure out how?


# Example: d([3,4],[0,0]) = 5.0
# Example: d([1,1],[0,0]) = 1.4142135623730951
# Example: d([1,1],[3,4]) = 3.605551275463989

# Example: circle(1000) = 802
# Example: circle(100000) = 78442
# Example: circle(123456) = 96979

from random import uniform
from math import sqrt

def d(p1,p2):
    sum = 0
    for i in range(len(p1)):
        sum += sqrt((p1[i]-p2[i])**2)
    return euclidean_d

def circle(n):
    center = [0,0]
    counter = 0
    for i in range(n):
        x = uniform(-1,1)
        y = uniform(-1,1)
        p1 = [x,y]
        if d(p1,center)<=1:
            counter += 1
    return counter
