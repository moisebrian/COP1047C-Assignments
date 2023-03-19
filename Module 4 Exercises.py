#!/usr/bin/env python3

#What is a variable?
	#containers for storing various data
#What is a constant?
	#constant are variables that stay consistant and cant be changed
#Can a variable be changed once assigned?
	#a variable can be assigned a new value
#Write a program that counts for the user. Let the user enter the starting number, the ending number, and the amount by which to count.

sales = ""
for sale in range(100,-10, (-10)):
	print(sale,end=" ")

	#Create a program that gets a message from the user and then prints it out backwards.
message = input("Any additional notes: ") [::-1]
print(message)


#Create a game where the computer picks a random word and the player has to guess that word. The computer tells the player how many letters are in the word. Then the player gets five chances to ask if a letter is in the word. The computer can only respond with “yes” or “no”. Then, the player must guess the word.
import random

# tuple of random words
RANDOM_WORDS = ("dog", "burger", "computer", "Biden", "python", "blue", "snake", "apple", "McNuggets", "Boba Tea", "weed", "lamborghini", "pizza", "basketball")

#pick one word randomly
word = random.choice(RANDOM_WORDS)
correct = word

#computer tells the player how many letters is in the random word
print("Im thinking of a word that has ", (len(word)), "letters in it.")

#player guess the word
guess = input("\nGuess a letter of the random word Im thinking of: ")
#the player gets five chances to ask if a letter is in the word
chance = 5

while ( chance > 1):
	chance -= 1
	for letter in guess:
		if letter.lower() in word:
			print("Yes")
		
		else:
			print("No")
	print("\nYou have", chance, "more chances to guess the correct letters.")
	guess = input("\nTake another guess: ")
chance -= 1

guess = input("\nGuess the word: ")
if guess == correct:
	print("\nYou guessed the correct word! Woohoo!")
else:
	print("\nUh-Oh, after 5 tries you still couldn't figure it out....bummer.")
print("\nThanks for playing.")
