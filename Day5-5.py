print("Welcome to PyPassword Generator")
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# easy
# password =""
# nr_letters = 6
# for char in range(1, nr_letters + 1): # 1 - 6
# password += random.choice(letters)
# random_char = random.choice(letters)
# password += random_char

# for char in range(1, nr_numbers + 1):
# password += random.choice(numbers)
# random_chr1 += random.choice(numbers)
# password += random_char1

# for char in range(1, nr_symbols + 1):
# password += random.choice(symbols)
# print(password)


########
# Hard
password_list = []
# nr_letters = 6
for char in range(1, nr_letters + 1):  # 1 - 6
    password_list.append(random.choice(letters))
# random_char = random.choice(letters)
# password += random_char

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
# random_chr1 += random.choice(numbers)
# password += random_char1

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f" YOr password is: {password}")
