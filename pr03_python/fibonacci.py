# Problem 2: Fibonacci Sequence
# Name: Ken Ma

# Introduction:
# Any term in the Fibonacci Sequence is found
# by adding the previous two terms.
# Example: 1, 1, 2, 3, 5, 8, 13, 21, 35

# Instructions:
# Input: some number, call it n
# Output: F_n (or the n^th Fibonacci Number)
# Note: The Fibonacci sequence is said to start with the
# 0^th number. So F_0 = 1, F_1 = 1, F_2 = 2, F_3 = 3, F_4 = 5, etc....

# Challnge Question: Print (F_n/F_{n-1}) as you go along: notice anything interesting?
n = int(input("Enter number here: "))
a = 1
b = 1
for i in range(1,n):
    c = a + b
    a = b
    b = c
print(c)
