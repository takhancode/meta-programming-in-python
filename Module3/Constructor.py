class student:
   def __init__(self, name, age):
        print("Hi i am talha")
        self.name = name
        self.age = age 
        
   def info(self):
        print("Name:", self.name)
        print("Age:", self.age)
            
        a= student("Talha", 20)
        b= student("Ali", 22)
        a.info()
        b.info()
        
        