# Task 17 - break statement in Python (NAVTTC Week 1)
# Reference: https://www.geeksforgeeks.org/python-break-statement/

# Example 1: break stops the loop completely
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Example 2: break inside a while loop
count = 0
while count < 10:
    if count == 4:
        break
    print(count)
    count += 1

# Example 3: stop at the first letter 'e'
for letter in "geeksforgeeks":
    if letter == 'e':
        break
print("Current letter:", letter)
