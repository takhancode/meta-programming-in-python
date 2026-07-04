# ?? Practice Task: Tuples in Python

# You are given the following tuple:

# fruits = ("apple", "banana", "mango", "orange", "banana")
# ?? Tasks:
# Print the entire tuple.
# Print the first and last element of the tuple.
# Find and print the element at index 2.
# Count how many times "banana" appears in the tuple.
# Find the length of the tuple.
# Try to change the first element to "grape" and observe what happens.
# ?? Bonus Challenge:
# Check if "mango" exists in the tuple and print:
# "Found" if it exists
# "Not Found" if it does not exist

fruits = ("apple", "banana", "mango", "orange", "banana")

# 1. Print entire tuple
print("Entire tuple:", fruits)

# 2. First and last element
print("First element:", fruits[0])
print("Last element:", fruits[-1])

# 3. Element at index 2
print("Index 2 element:", fruits[2])

# 4. Count banana occurrences
count = 0
for fruit in fruits:
    if fruit == "banana":
        count += 1

print("banana appears", count, "times")

# 5. Length of tuple
print("Length:", len(fruits))

# 6. Tuple is immutable (cannot change)
# fruits[0] = "grape"   This will cause error

# 7. Check if mango exists
if "mango" in fruits:
    print("Found")
else:
    print("Not Found")
