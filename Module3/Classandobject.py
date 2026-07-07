class person: 
 name = "John"
 occupation = "Engineer"
 networth = 1000000
 def info(self):
  print("Name:", self.name)
  print("Occupation:", self.occupation)
  print("Net Worth:", self.networth)
  
  a=person()
  b=person()
  c=person()
  
  
  a.name = "Alice"
  a.occupation = "Doctor"
  a.networth = 2000000
  
  
  b.name = "Bob"
  b.occupation = "Artist"
  b.networth = 500000
  
  print("Person A Info:")
  a.info()
  print("\nPerson B Info:")
  b.info()