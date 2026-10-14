# Task 16 - while loops in Python (NAVTTC Week 1)
# Reference: https://www.geeksforgeeks.org/python-while-loops/

# Example 1: basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Example 2: while loop with else
i = 1
while i < 4:
    print(i)
    i += 1
else:
    print("Loop finished!")

# Example 3: sum of numbers from 1 to 10
total = 0
n = 1
while n <= 10:
    total = total + n
    n += 1
print("Sum is", total)
