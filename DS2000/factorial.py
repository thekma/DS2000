# Problem 1: Factorial
# Name: Ken Ma

# Introduction:
# n! (said "n factorial") is found by multiplying n and all natural numbers
# less than n
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# Example: 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3,628,800

# Instructions:
# Input: some number, call it n
# Output: n! (or n factorial)
n = int(input("Enter number: "))
num = 1
for i in range(1,n+1):
    num = num * i
print(str(n)+"! = ",num)
