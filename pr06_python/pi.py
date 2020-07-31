# Problem 3: Pi Revisted
# Name:

# Introduction: Last week, we built 3 pi approximations. The code for those
# approximations are below. Sometimes, it is useful to have several pieces of information
# returned from a function rather than just one. This week, we are going to practice that a bit

# Instructions: You should build a fourth function (compare(epsilon)) that inputs some
# epsilon, runs all three pi approximations, and tells you which got within the
# epsilon the fastest (i.e. had the smallest counter) and also tells me what the approximation
# was.
# Note: You will need to modify my code just a tiny bit before building your function.


# Example: compare(0.0000001) = 'pi1 got there the fastest with an approximation of pi = 3.1415925535897995'
# Example: compare(0.00001) = 'pi1 got there the fastest with an approximation of pi = 3.1415826536298037'
# Example: compare(0.001) = 'pi1 got there the fastest with an approximation of pi = 3.140593091569114'


from math import pi
from math import sqrt
from random import uniform

def pi1(epsilon):
    piApprox = 0
    i = 0
    while abs(piApprox-pi)>epsilon:
        piApprox += (-1)**(i) * (4 / (2*i+1))
        i += 1
    return(i)

def pi2(epsilon):
    sum = 0
    piApprox = 0
    i = 1
    while abs(piApprox-pi)>epsilon:
        sum += 6/(i**2)
        piApprox = sqrt(sum)
        i += 1
    return(i-1)

def pi3(epsilon):
    piApprox = 1
    i = 0
    c1 = 0
    c2 = 1
    num = 0
    dem = 1
    while abs(2*piApprox-pi)>epsilon:
        if c1 % 2 == 0:
            num += 2
        if c2 % 2 == 0:
            dem += 2
        piApprox *= num/dem
        c1 += 1
        c2 += 1
        i += 1
    return(i)


