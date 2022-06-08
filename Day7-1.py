import random
# step1
word_list = ["evolution", "canada", "farmer", "advance"]
the_word = random.choice(word_list)
the_blank = len(the_word)

# testing code
print(f"Past, the solution is {the_word}")

display = []
# for letter in the_word:
for _ in range(the_blank):
    display += "_"
print(display)

the_guess = input("please enter your guess's letter:").lower()
# for letter in the_word:
for position in range(the_blank):
    letter = the_word[position]
    if letter == the_guess:
        display[position] = letter
        print(display)


