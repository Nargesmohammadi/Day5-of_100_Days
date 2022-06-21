programing_dictionary = {
    "Bug": "An error in a program that prevents the program form running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programing_dictionary["Function"])

# Adding new items to dictionary.
programing_dictionary["Loop"] = "The action of doing something over and over again."

# print(programing_dictionary)
# Create an empty dictionary.
empty_dictionary = {}

# Wipe an existing dictionary
# programing_dictionary = {}
# print(programing_dictionary)

# Edit an item in a dictionary
programing_dictionary["Bug"] = "A moth in your computer"
print(programing_dictionary)

# Loop through a dictionary
for thing in programing_dictionary:
    print(thing)

for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])
