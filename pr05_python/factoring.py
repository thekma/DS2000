# Problem 3: Unique Factorization of a Number
# Name:

# Introduction:
# Website: https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
# Every positive integer n has a unique factorization into prime numbers. In this sense, primes
# are thought of as the "building blocks" of numbers.
# (Reminder: a prime number is an integer divisible by only 1 and itself)
# In today's program, we are going to use our SOE to find the unique prime factorization
# of a positive integer.
# Example: 15 = 3 * 5
# Example: 12 = 2 * 2 * 3
# Example: 120 = 2 * 2 * 2 * 3 * 5
# Example: 42 = 2 * 3 * 7


# Instructions: You should input a positive integer n.
# The output should be a SORTED list of prime numbers that, when multiplied togther,
# givess n.

#NOTE: You should use a while loop in this program.

# Example: factor(12) = [2, 2, 3]
# Example: factor(52) = [2, 2, 13]
# Example: factor(1234) = [2, 617]
# Example: factor(12345) = [3, 5, 823]
# Example: factor(123456) = [2, 2, 2, 2, 2, 2, 3, 643]

def factor(n):
    for i in range(1,10):
        if n % i = 0:
            ff = n // i
            if ff == 1:
                return 1
        else:
            return n
