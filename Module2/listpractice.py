# ?? Practice Task: Python List

# You are given the following list:

# numbers = [12, 45, 7, 89, 34, 45, 23]
# ?? Tasks:
# Print the entire list.
# Print the first and last element of the list.
# Change the value of the 3rd element to 100.
# Add a new number 50 at the end of the list.
# Remove the number 45 from the list (first occurrence only).
# Print the updated list.

numbers = [12, 45, 7, 89, 34, 45, 23]
print("Entire list:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])
numbers[2] = 100
numbers.append(50)
numbers.remove(45)
print("Updated list:", numbers)
