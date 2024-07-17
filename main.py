import random
import hangman_art
import hangman_words
import os
def clear_console():
    """Clear the console based on the operating system."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-like systems (Linux, macOS, etc.)
        os.system('clear')

design = hangman_art.logo
print(design)
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
blank = []
for _ in range(len(chosen_word)):
    blank +="_"
#cprint(blank)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Enter the word").lower()
    clear_console()
    for position in range(len(chosen_word)):
        later = chosen_word[position]
        if later == guess:
            blank[position] = later
    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            end_of_game = True
            print("You lose!")
    print(blank)
    if "_" not in blank:
        end_of_game = True
        print("You win!")
    print(hangman_art.stages[lives])