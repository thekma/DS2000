# Problem 4: Multiplying Lists
# Name: Ken Ma

# Introduction: We are given two lists.
# The goal is to take all multiplications of all elements in list 1
# with all elements in list 2
# Example: List1 = [1,2,3], List2 = [4,5,6]
# [4,5,6,8,10,12,15,18]

# Instructions:
# Input: Two separate lists (inputted as integers, separated by spaces)
# Hint: use "split"
# Output: One list, that has all the products in it, with no repeats
# Example: Notice that 2 * 6 = 12 = 3 * 4, would have appeared twice in the example above
# We only want to put it in the list once.
mlin_list1 = input("First list: ").split()
mlin_list2 = input("Second list: ").split()
sam = []
for a in mlin_list1:
    for b in mlin_list2:
        mult = int(a) * int(b)
        if mult not in sam:
            sam.append(mult)
print(sam)
