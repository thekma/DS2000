# Problem 1: Vectors
# Name:

# Introduction: A vector is a mathematical object that has both magnitude and direction
# Basically, it's a line in space with some length that points in some direction
# It is of interest, given a vector in two dimensions [x,y],
# to find its magnitude and direction
# One can do this in the following way:
# Magnitude = sqrt(x^2 + y^2)
# Direction = arctan(y/x)


# Instructions: Build a function (vector(v)) that inputs a vector v
# in list for [x,y] and returns BOTH the magnitude and direction

# Note: You will need the sqrt from the math module and
# arctan, you can find in the numpy module
# Additionally, the direction will be returned in terms of radians.
# To get it in terms of degrees (so it is easier to visualize), you will
# want to divide your answer by pi and multiply by 180.

# Challenge Question: The ArcTan has a domain issue. Specifically, rather than being allowed
# to "roam freely," it will ever only return an answer between -pi/2 (-90 degrees)
# and pi/2 (90 degrees). Can you help your function figure out how to deal with this?
# Hint: You will have to look at the respective parity (i.e. positive/negativeness)
# of your x and y coordinates.


# Example: vector([3,4]) = (5.0, 29.516723530086651)
# Example: vector([1,2]) = (2.23606797749979, 35.241638234956682)
# Example: vector([1/2,sqrt(3)/2]) = (0.9999999999999999, 33.333333333333336)

from numpy import arctan
from math import sqrt
from math import pi

def vector(v):
    x2 = v[0]
    y2 = v[1]
    d = sqrt(x2**2 + y2**2)
    a = (arctan(y / x))/pi*180
    return(d,a)
