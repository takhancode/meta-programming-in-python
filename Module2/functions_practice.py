# Module 2 - Functions Practice

# 1. Simple Function
def greet(name):
    print(f"Hello, {name}!")

# 2. Function with Return
def add_numbers(a, b):
    return a + b

# 3. Function with Default Value
def introduce(name, age=18):
    print(f"My name is {name} and I am {age} years old.")

# 4. Function with Multiple Returns
def calculator(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    return add, subtract, multiply

# Testing all functions
greet("Talha")
print(add_numbers(5, 10))
introduce("Talha", 20)
print(calculator(10, 5))