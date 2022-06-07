import random
word_list = ["evolution", "canada", "farmer", "advance"]
the_word = random.choice(word_list)
the_blank = len(the_word)
print(f"Past, the solution is {the_word}")

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 'n', "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
the_guess = input("please enter your guess's letter:").lower()
for letter in the_word:
    if letter == the_guess:
        print("right")
    else:
        print("wrong")
