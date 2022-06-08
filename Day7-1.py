import random

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
  ===''', '''
   +---+
   O   |
       |
       |
  ===''', '''
   +---+
   O   |
   |   |
       |
  ===''', '''
   +---+
   O   |
  /|   |
       |
  ===''', '''
   +---+
   O   |
  /|\  |
       |
  ===''', '''
   +---+
   O   |
  /|\  |
  /    |
  ===
''', '''
   +---+
   O   |
  /|\  |
  / \  |
  ===
  ''', '''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
  ===''']

# step1
word_list = ["evolution", "canada", "farmer", "advance"]
the_word = random.choice(word_list)
the_blank = len(the_word)

lives = []

# testing code
print(f"Past, the solution is {the_word}")

display = []
# for letter in the_word:
for _ in range(the_blank):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    the_guess = input("please enter your guess's letter:").lower()
    # for letter in the_word:
    for position in range(the_blank):
        letter = the_word[position]
        if letter == the_guess:
            display[position] = letter

if the_guess not in the_word:
    lives -= 1
    if letter == 0:
        end_of_game = True
        print("You loss")
print(display)

if "_" not in display:
    end_of_game = True
    print("You win")


print(HANGMAN_PICS[lives])