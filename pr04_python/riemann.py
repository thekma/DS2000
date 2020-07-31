# Problem 1: Riemann Zeta Function
# Name: Ken Ma

# Introduction:
# Website: https://simple.wikipedia.org/wiki/Riemann_zeta_function
# The Riemann Zeta Function is, in simple terms, the sum of 1/(n^s),
# where n ranges from 1 to k (as k tends towards infinity) and s is given.
# Since it is impossible to let k -> infinity (on a computer),
# we will instead allow k to be some number of our choosing

# Example: s = 1, k = 5, we obtain 1/1 + 1/2 + 1/3 + 1/4 + 1/5
# = 1/(1^1) + 1/(2^1) + 1/(3^1)+ 1/(4^1) + 1/(5^1)
# = 2.28333....
# Example: s = 3, k = 4, we obtain 1/1 + 1/8 + 1/27 + 1/64
# = 1/(1^3) + 1/(2^3) + 1/(3^3)+ 1/(4^3)
# = 1.42361....
# Example: s = 5, k = 3, we ontain 1/1 + 1/32 + 1/243
# = 1/(1^5) + 1/(2^5) + 1/(3^5)
# = 1.03537....

# Instructions: Today, we are going to create a FUNCTION (RiemannZeta(s,k)) that
# inputs: s (the power on the terms) and k (the number of terms)
# returns: the decimal approximation for function.

# Example: RiemannZeta(1,100) = 5.187377517639621
# Example: RiemannZeta(4,500) = 1.0823232310524604
# Example: RiemannZeta(2,10000) = 1.6448340718480652

def riemann(s,k):
    sum = 0
    for i in range(1,k+1):
        value = 1/((i)**s)
        sum += value
    return sum
