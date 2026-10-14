# Task 18 - continue statement in Python (NAVTTC Week 1)
# Reference: https://www.geeksforgeeks.org/python-continue-statement/

# Example 1: continue skips only the current iteration
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Example 2: print only odd numbers
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)

# Example 3: skip the letter 'e'
for letter in "geeksforgeeks":
    if letter == 'e':
        continue
    print(letter, end=' ')
print()
