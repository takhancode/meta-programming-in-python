# By Slicing method
text = "Hello, World!"
reversed_text = text[::-1]
print(reversed_text)  # Output: !dlroW ,olleH

# By Loop method
text = "Hello, World!"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(reversed_text)  # Output: !dlroW ,olleH


#By Reverse method
text = "Hello, World!"
reversed_text = ''.join(reversed(text))
print(reversed_text)  # Output: !dlroW ,olleH
 