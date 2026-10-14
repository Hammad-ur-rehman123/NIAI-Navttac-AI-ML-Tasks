# Task 15 - for loops in Python (NAVTTC Week 1)
# Reference: https://www.geeksforgeeks.org/python-for-loops/

# Example 1: for loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 2: for loop with range()
for i in range(5):
    print(i)

# Example 3: range(start, stop, step)
for i in range(2, 10, 2):
    print(i)

# Example 4: for loop over a string
for ch in "python":
    print(ch)

# Example 5: nested for loop
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
