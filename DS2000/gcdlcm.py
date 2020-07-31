# Problem 3: Greatest Common Divisor and Least Common Multiple
# Name: Ken Ma

# Introduction:
# Website: https://en.wikipedia.org/wiki/Greatest_common_divisor
# Website: https://en.wikipedia.org/wiki/Least_common_multiple
# The greatest common divisor (GCD) and least common multiple (LCM) between two
# numbers are some of the most important mathematical relations between two numbers
# We'll start by picking two integers, call them a and b.
# The greatest common divisor of a and b is the largest number that divides both of them
# The least common multiple of a and b is the smallest number that both a and b divides
# Example: the GCD of 14 and 6 is 2, and the LCM of 14 and 6 is 42.
# Example: the GCD of 25 and 15 is 5, and the LCM of 25 and 15 is 75

# Instructions: We are going to create two FUNCTIONS (gcd(a,b) and lcm(a,b)) that takes integers
# inputs: a and b and
# outputs: their GCD and LCM, respectivelyself.
# We will do this using the Euclidean Algorithm. To see an example, let a = 28 and b = 18:
# Step 1: is a >= b? If not, trade their roles
# Step 2: does b divide a? If so, b is the GCD
#               if not, then write a as a = m * b + r
# r is what we call the remainder: 28 = 18 + 10
# Step 3: set a = b and b = r. Then repeat the process.
# 18 = 10 + 8
# 10 = 8 + 2
# 2 divides 8, so 2 is the GCD of 28 and 18

# Example: a = 30, b = 21
# 30 = 21 + 9 -- set a = 21 and b = 9
# 21 = 9*2 +3 -- set a = 9 and b = 3
# 3 divides 9, so 3 is the GCD of 30 and 21

# Example: a = 51, b = 11
# 51 = 11*4 + 7 -- set a = 11 and b = 7
# 11 = 7 + 4 -- set a = 7 and b = 4
# 7 = 4 + 3 -- set a = 4 and b = 3
# 4 = 3 + 1 -- set a = 3 and b = 1
# 1 divides 3, so 1 is the GCD of 51 and 11.

# To find the LMC, just note that LCM(a,b) * GCD(a,b) = a*b.


# Example: gcd(421312,53242) = 2, lcm(421312,53242) = 11215746752
# Example: gcd(5400,960) = 120, lcm(5400,960) = 43200
# Example: gcd(100000,1401974816) = 32, lcm(100000,1401974816) = 4381171300000

# Extra Challenge Question: If the GCD of two numbers is one, the two numbers
# are called relatively prime. (https://en.wikipedia.org/wiki/Coprime_integers)
# Can you create a function that tells you the number of positive integers less than
# some input n that are relatively prime to n? This is called the Euler Totient Function
# https://en.wikipedia.org/wiki/Euler%27s_totient_function

def gcd(x,y):
    a = max(x,y)
    b = min(x,y)
    for i in range(a):
        if a%b != 0:
            c = a%b
            a = b
            b = c
        else:
            return b

def lcm(x,y):
    return (a*b) // gcd(a,b)
