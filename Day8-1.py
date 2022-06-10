# # # Create a function called greet().


# # simple function

# def greet():
# print("Hello Mitra")
# print("How do you do Melo?")
# print("Isn't the weather nice today?")


# print(greet())


# # function that allows for input

# def greet_with_name(name):
# print(f"Hello {name}")
# print(f"How do you do {name}?")
# print("Isn't the weather nice today?")


# greet_with_name("Mitra")

# # function with more than one input.

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location}")


# greet_with("Mitra", "Shiraz")
# greet_with("Shiraz", "Mitra")

# # functions with keyword arguments

greet_with(name="Mitra", location="Shiraz")
greet_with(location="Shiraz", name="Mitra")


# # # Write 3 print statements inside the function.
# # # Call the greet() function and run your code.
