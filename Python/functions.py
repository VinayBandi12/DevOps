#Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("Hello Vinay")
  print("How are you Vinay?")
  print("Isn't the weather nice today")

greet()

def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How are you {name}?")
  print("Isn't the weather nice today")

greet_with_name("Angela")

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"How are you {name}?")
  print(f"Isn't the weather nice today in {location}")

greet_with("Vinay", "New York")

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"How are you {name}?")
  print(f"Isn't the weather nice today in {location}")

greet_with(location= "New York", name = "Vinay")