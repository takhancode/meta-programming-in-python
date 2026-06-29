student={
    "name":"ali" , 
    "age" : 20  ,
    "grade" : "A"
}


# Acessing the dictionary
print(student["name"])

# Adding a new keyvalue pair
student["city"]="lahore"

# Updating a value
student["age"]=22

# Removing an item
del student["age"]

for key in student:
    print(key)
for value in student.values:
   print(value)


# for both key and value
for key,value in student.items:
    print(key,value)
