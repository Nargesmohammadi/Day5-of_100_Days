import random

# step1
# word_list = ["evolution", "canada", "farmer", "advance"]
from hangman_words import word_list

the_word = random.choice(word_list)
the_blank = len(the_word)
the_chance = len(HANGMAN_PICS)

end_of_game = False

lives = 8

from hanngman_art import logo, stages

print(logo)

# testing code
print(f"Past, the solution is {the_word}")

display = []
# for letter in the_word:
for _ in range(the_blank):
    display += "_"
print(display)

while not end_of_game:
    the_guess = input("please enter your guess's letter:").lower()

    clear()
    if the_guess in display:
        print(f'you already guessed {the_guess}')

    # for letter in the_word:
    for position in range(the_blank):
        letter = the_word[position]
        if letter == the_guess:
            display[position] = letter

if the_guess not in the_word:
    print(f"You guessed {the_guess}, that's not in the word. You loss a life.")
    lives -= 1
    if letter == 0:
        end_of_game = True
        print("You loss")
print(display)

if "_" not in display:
    end_of_game = True
    print("You win")

print(stages[lives])
