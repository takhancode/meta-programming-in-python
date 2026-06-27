# 🧪 Practice Task: Sets in Python

# You are given the following set:

# numbers = {10, 20, 30, 40, 50, 20, 30}
# 🔹 Tasks:
# Print the set.
# Add a new number 60 to the set.
# Remove the number 20 from the set.
# Try to add a duplicate value 30 and observe what happens.
# Check if 40 exists in the set and print "Found" or "Not Found".
# Print the length of the set.
# 🔥 Bonus Challenge:
# Create another set:
# more_numbers = {30, 40, 70, 80}

# 👉 Perform:

# Union of both sets
# Intersection of both sets
 
numbers = {10, 20, 30, 40, 50, 20, 30}

# 1. Print set
print("Original set:", numbers)

# 2. Add 60
numbers.add(60)

# 3. Remove 20
numbers.remove(20)

# 4. Try duplicate add
numbers.add(30)

print("After operations:", numbers)

# 5. Check if 40 exists
if 40 in numbers:
    print("Found")
else:
    print("Not Found")

# 6. Length of set
print("Length:", len(numbers))

# Bonus
more_numbers = {30, 40, 70, 80}

# Union
print("Union:", numbers | more_numbers)

# Intersection
print("Intersection:", numbers & more_numbers)