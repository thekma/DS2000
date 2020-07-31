# Problem 4: Binary
# Name: Ken Ma

# Introduction: Binary is the shorthand way of saying "base two".
# Generally, we work in a base 10 world. That is to say, every "place holder"
# in a number means an extra base. Specifically,
# 594231 = 1 * 10^0 + 3 * 10^1 + 2 * 10^2 + 4 * 10^3 + 9 * 10^4 + 5 * 10^5
# If I want to switch to base 2, we would instead of working with 10's, work with powers of 2
# 101011 = 1* 2^0 + 1 * 2^1 + 0 * 2^2 + 1 * 2^3 + 0 * 2^4 + 1 * 2^5
# (or 43, in standard base 10)
# Website: https://en.wikipedia.org/wiki/Binary_number
# Binary is used in computers, because it only works with 1's and 0's (in base 2, no other numbers exist)
# Therefore, a computer can interpret something like 101 as (on-off-on), where the "on"
# corresponds with different spurts of electricity, and "off" has no power

# Instructions 1: Build a function (call it "binary(k)") where you input string
# of ones and zeros, and the function returns the base ten representation of that binary string

# Instructions 2: In a 8-bit system, usually we make sure that every binary number has
# a combination of 8 zeros and ones, adding zeros as necessary.
# For example, 1000110 only has seven ones and zeros, so we would change it to
# 01000110 and 0101 would become 00000101.
# Edit your code above to do this for a 8-bit system.
# It should be an easy modification from there to work for ANY-bit system.

# Why is this important? Because of the ASCII language? Specifically, that translates any letter into
# binary strings of length 8: see http://sticksandstones.kstrom.com/appen.html

# Instructions 3: Create a third function that uses LIST COMPREHENSION to return all
# the binary expansion of all multiples of 10
# less than 200 as a list. (i.e. 0, 10, 20, 30, 40, 50, ect...)




# Challenge Question #1: # Build another function (call it "yranib(n)") that undoes what you did above
# Specifically, if you input a base 10 number, return a string of 1's and 0's (read from left to right)
# that is the binary representation of that number

# Challenge Question #2: Can you extend this code to any base? That is to say
# build a new function, call it multinary(base,n) that inputs a
# number n and base and writes the number n in that new base
# Can you write a similar function (call it yranitlum(base,n)) that undoes your new function?

# Challenge Question #3: Can you build a function that, without changing bases,
# multiplies two numbers in base 2 together and returns a number in base 2?

# Example: binary(100) = '1100100'
# Example: binary(1234) = '10011010010'
# Example: binary(214) = '11010110'

# Example: eightbit(100) = '01100100'
# Example: eightbit(15) = '00001111'
# Example: eightbit(22) = '00010110'

# Example: listComprehension(200) = ['0', '1010', '10100', '11110', '101000', '110010', '111100', '1000110', '1010000', '1011010', '1100100', '1101110', '1111000', '10000010', '10001100', '10010110', '10100000', '10101010', '10110100', '10111110', '11001000']

# Example: yranib('1100100') = 100
# Example: yranib('10011010010') = 1234
# Example: yranib('11010110') = 214

def yranib(onesandzeros):
    num_list = list(onesandzeros)
    sum = 0
    for num_i in range(len(onesandzeros)):
        sum_part = int(num_list[num_i])*(2**(abs(num_i - (len(onesandzeros)-1))))
        sum += sum_part
    return sum
