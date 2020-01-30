import random
import sys

wordList = [
"lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
]

guessWord = []
secWord = random.choice(wordList)
wordLen = len(secWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letStorage = []

def beginning():
	
	print("HANGMAN")

	

	while True:

		name = input("Enter Name")

		if name == '':
			print("Try again")
		else:
			break

beginning()

def newFunc():
    print("Well, that's perfect moment to play some Hangman!\n")

    while True:
        gameChoice = input("Would You?\n").upper()

        if gameChoice == "YES" or gameChoice == "Y":
            break
        elif gameChoice == "NO" or gameChoice == "N":
            sys.exit("That's a shame! Have a nice day")
        else:
            print("Please Answer only Yes or No")
            continue

newFunc()

def change():

	for character in secWord:
		guessWord.append("-")

	print("Ok, so the word You need to guess has", wordLen, "characters")

	print(guessWord)


def guessing():

	guessTaken = 1

	while guessTaken < 10:

		guess = input("Pick a letter").lower()

		if not guess in alphabet:
			print("Enter a valid letter")
		elif guess in letStorage:
			print("You guessed already")
		else:

			letStorage.append(guess)
			if guess in secWord:
				print("You Guessed correctly")
				for x in range (0, wordLen):
					if secWord[x] == guessTaken:
						guessWord[x] = guess
						print(guessWord)

				if not '-' in guessWord:
					print("You won")
					break
			
			else:
				print("Letter not in word")
				guessTaken+=1
				if guessTaken == 10:
					print("You lost, Secret word was ", secWord)

change()
guessing()

print("Game Over")
























