# Creating a file with w mode
file = open('sample.txt', 'w')
file.write("Hello World!")
file.close()

# Creating a file with context manager (safer)
with open('test.txt', 'w') as file:
    file.write("Hello World")

# Creating a file in exclusive creation mode (x)
with open('newfile.txt', 'x') as file:
    file.write("This is a new file")

# Creating a file and writing multiple lines
with open('multiline.txt', 'w') as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")

# Creating a file with writelines
with open('lines.txt', 'w') as file:
    lines = ["First line\n", "Second line\n", "Third line\n"]
    file.writelines(lines)

# Appending to an existing file
with open('sample.txt', 'a') as file:
    file.write("\nAppended text")

# Reading from a file
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)
    