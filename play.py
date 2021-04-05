import hangman
import string

secret_word = "apple"
guesses_remaining = 6

# The game starts.
print("Welcome the game Hangman!")
print("--Made by Ali Dereyurt--")
print("------------------------")
print("The secret word has " + str(len(secret_word)) + " letters.")
print("You have " + str(guesses_remaining) + " guesses. Good luck!")
input_letter = input("Please guess a letter: ")



print(string.ascii_lowercase)