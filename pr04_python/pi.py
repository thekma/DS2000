# Problem 2: Approximating Pi
# Name: Ken Ma

# Introduction:
# Website: https://en.wikipedia.org/wiki/Pi#Infinite_series
# Today will be one of the attempts we will use to try to approximate pi
# Pi is a famous mathemtical constant that can be calculated by measuring the
# circumference of a circle of diameter 1
# It is well known that pi = 3.1415926....
# One of many ways to approximate pi is by using a famous infinite series, specifically
# pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + 4/13 - 4/15 + 4/17 -....

# Instructions: We are going to create a FUNCTION (PI(k)) that takes
# inputs: k, where k is the number of terms in our approximation and
# outputs: our approximation

# Example: PI(10) = 3.0418396189294032
# Example: PI(100) = 3.1315929035585537
# Example: PI(1000) = 3.140592653839794

# Extra Challenge Question: How many terms would you need to sum before your approximation
# for pi is accurate to 13 decimal places? Can you make a program that generalizes
# this question for any number of decimal places?
# note, you can obtain pi with the following code: from math import pi
# and then inputting pi

n = 0
def PI(k):
    sum = 0
    for r in range(1,n+1):
        sum += (-1)**(r+1)*(4/(2*r-1))
    return sum

def PI2(k):
    pi = 0
    num = 4
    dem = 1
    for i in range(k):
        if i % 2 == 0:
            pi += num/dem
        else:
            pi -= num/dem
        dem+= 2
    return pi
