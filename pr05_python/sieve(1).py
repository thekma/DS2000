# Problem 2: Sieve of Eranthoses
# Name:

# Introduction:
# Website: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# An important construct in mathematics is that of the "prime numbers"
# A number is prime if and only if its only divisors are itself and 1
# For example, 7 is prime because only 7 and 1 divide 7.
# However, 6 is not prime because both 2 and 3 divide 6.
# The Sieve of Eranthoses is a quick way to generate a list of primes
# What the sieve does is that it starts with a list of numbers,
# takes the first number in the list, and then removes all the multiples of that numbers
# but leaves the first number
# Example: [2,3,4,5,6,7,8,9,10,11,12] --> [2,3,7,9,11], since all the others are multiples of 2
# [2,3,5,7,9,11] --> [2,3,5,7,11] since 9 is divisible by the next number (3)
# 7 and 11 do not divide any numbers in the list, so we are done.
# Note that 2, 3, 5, 7, 11 are the first five primes

# Instructions: We are going to impliment this algorithm. We will input a number n,
# which will tell us what what we want to find all the primes up to:
# for example, [2,3,5,7,11] is all the primes up to 12.
# Our function (call it SOE(n)) will output a list with all the primes up to (and including) n
# NOTE: IN ORDER TO GET PRIMES, YOUR STARTING LIST MUST LOOK LIKE
# [2,3,4,5,6,.....,n-1,n]


# Example: SOE(20) = [2, 3, 5, 7]
# Example: SOE(50) = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
# Example: SOE(100) = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def SOE(n):
