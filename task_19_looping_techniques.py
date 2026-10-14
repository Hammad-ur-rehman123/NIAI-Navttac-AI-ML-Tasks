# Task 19 - Looping techniques in Python (NAVTTC Week 1)
# Reference: https://www.geeksforgeeks.org/looping-techniques-python/

# Example 1: enumerate() - loop with index
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Example 2: zip() - loop through two lists together
names = ["Ali", "Sara"]
ages = [20, 22]
for name, age in zip(names, ages):
    print(name, age)

# Example 3: looping through a dictionary
d = {"a": 1, "b": 2}
for key, value in d.items():
    print(key, value)

# Example 4: reversed() - loop in reverse order
for i in reversed(range(5)):
    print(i)

# Example 5: sorted() - loop through sorted values
nums = [3, 1, 4, 1, 5]
for n in sorted(nums):
    print(n)
