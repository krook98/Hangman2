import random
import os
from words import word_list
from art import logo
from art import stages

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
end_of_game = False
display = []
guessed = []

for letter in chosen_word:
    display.append("_")
print(display)

while not end_of_game:
    guess = input("Please guess the letter").lower()
    clean = lambda: os.system('cls')
    clean()
    if guess in guessed:
        print(f"You've already guessed {guess}")
        continue
    else:
        guessed += guess
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print("You lost!")
            end_of_game = True
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(display)
