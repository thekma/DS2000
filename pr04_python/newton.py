# Problem 5: Newton's Method
# Name: Ken Ma

# Introduction:
# Website: https://en.wikipedia.org/wiki/Newton%27s_method
# Newton's Method is a technique for finding the zeros of a function.
# That is, if you have a function f(x), Newton's Method allows you to find
# x such that f(x) = 0.
# Essentially, you pick some starting point x_0, and then you let
# x_1 = x_0 - f(x_0)/fprime(x_0)

# Instructions: You will need to create 3 functions. One that is your base functions
# (call it f(x)) and another that its derivative (call it fprime(x)). If you do not know
# what the derivative is, that is not important for coding this. The 3rd function will impliment
# Newton's Method. Call this function Newton(n,x_0), where n is the number of iterations
# and x_0 is the starting point.
# You will use the following algorithm: you pick some starting point x_0, and then you let
# x_1 = x_0 - f(x_0)/fprime(x_0)
# x_2 = x_1 - f(x_1)/fprime(x_1)
# x_3 = x_2 - f(x_2)/fprime(x_2)
# you will repeat this n times.

# For each of the following examples, play around with the different starting points.
# You can get different zeros, depending on where you start. Interesting, eh?


# Example:
# f(x) = x^3 - 16 x^2 + 65 x - 50
# fprime(x) = 3 x^2 - 32 x + 65
# newton(10,21) = 10.0

# Example:
# f(x) = x^4 -127 x^2 + 234 x + 360
# fprime(x) = 4 x^3 - 254 x + 234
# newton(3,0) = -1.000734213082633

# Example: you will need to import sin and cos from math
# f(x) = sin(x)
# fprime(x) = cos(x)
# newton(4,2) = 3.1409439123176353

from math import sin
from math import cos
def f(x):
    return x**3 - 16*x**2 + 6*x - 50

def fprime(x):
    return cos(x)

def Newton(n, x_0):
    for i in range(n):
        x_0 = x_0 - 16
