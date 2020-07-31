# Problem 3: Collatz Conjecture
# Name: Ken Ma

# Introduction:
# The rules for this game is simple
# if a number is even, divide it by 2
# if a number is odd, multiply by 3 and add 1.
# Example: 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# Example: 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# Instructions:
# Input: some numbers, call them n and k
# Output: Run the following game k times starting with the number n,
# printing each number it obtains along the way
# The two examples above were "run" 6 times and 14 times, respectively.
# Challenge Question: Can you see a certain pattern that it always returns to?
# If so, can you change your code to tell you how long before it hits that pattern?
n = int(input("Starting number: "))
k = int(input("How many times: "))
for i in range(1,k+1):
    if n%2 == 0:
        n = int(n/2)
    else:
        n = (n*3)+1
    print("The "+str(i)+"th number in this is ",int(n))
