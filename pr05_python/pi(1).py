# Problem 1: Pi Approximations
# Name: Ken Ma

# Introduction: In this program, we will be using three different ways to approximate pi
# Method 1: pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + 4/13 -.....
# Method 2: pi = sqrt( 6/1^2 + 6/2^2 + 6/3^2 + 6/4^2 + 6/5^2 +....) = sqrt(6/1 + 6/4 + 6/9 + 6/16 + 6/25 + 6/36 + ...)
# Method 3: pi = 2 *(2/1 * 2/3 * 4/3 * 4/5 * 6/5 * 6/7 * 8/7 * 8/9 * 10/9 * 10/11 *....)
# However, instead of computing n terms, we will instead compute until we are within some
# epsilon of pi. That is to say, we want to do this until the difference our approximation
# and pi is less than epsilon
# e.g. abs(piApprox - pi) < epsilon

# Instructions: For each of the three pi approximations above, you should build a function that
# inputs some epsilon, and returns the number of iterations we needed until our approximation
# was within epsilon of pi
# Specifically, abs(pi-piApprox)<epsilon

# Hint: You can find pi in the math module. Specifically, "from math import pi"


# Example: pi1(0.00001) = 100001
# Example: pi2(0.00001) = 95493
# Example pi3(0.00001) = 157079

# Example: pi1(0.0000123) = 81301
# Example: pi2(0.0000123) = 77637
# Example pi3(0.0000123) = 127706

from math import pi
from math import sqrt

def pi1(epsilon):
    piapprox = 0
    k = 0
    while abs(piapprox-pi)>epsilon:
        piapprox += (-1)**(k)*(4/(2*k+1))
        k += 1
    return (k)

def pi2(epsilon):
    sum = 0
    piapproxim = 0
    ii = 0
    while abs(piapproxim-pi)>epsilon:
        sum += 6/((ii+1)**2)
        ii += 1
        piapproxim = sqrt(sum)
    return (ii)

def pi3(epsilon):
    return 0 #skipped
