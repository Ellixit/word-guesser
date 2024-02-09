import random
import json

def main():
    userName = input("What's your name? ")
    print("Hello, " + userName + "!")
    while True:
        gameDriver()
        userInput = input("Would you like to play again? ")
        if userInput.lower() == "yes":
            continue
        else:
            break

def gameDriver():
    numGuesses = 0

    #Choose difficulty, determines number of guesses allowed
    while True:
        userInput = input("\nWould you like to play on easy, normal, or hard difficulty? ")
        if userInput.lower() == "easy":
            numGuesses = 15
            break
        elif userInput.lower() == "normal":
            numGuesses = 10
            break
        elif userInput.lower() == "hard":
            numGuesses = 5
            break
        else:
            print("Option not available, please try again.")

    print ("\nYou will have " + str(numGuesses) + " turns.")

    #Set of words, may replace with json file
    from pathlib import Path
    p = Path(__file__).with_name('wordbank.json')
    with p.open('r') as json_file:
        wordList = json.load(json_file)

    guessedLetters = {""}
    wordLetters = {""}

    #Chooses word randomly from set of words
    keyWord = wordList[round(random.uniform(0, len(wordList) - 1))]

    #Stores letters in word into a set
    for i in range(len(keyWord)):
        currentChar = keyWord[i].upper()
        if currentChar in guessedLetters:
            continue
        else:
            wordLetters.add(currentChar)

    #Loop for guessing mechanism
    while True:
        blankCounter = 0
        print("")
        for i in range(len(keyWord)):
            currentChar = keyWord[i].upper()
            if currentChar in guessedLetters:
                print(currentChar, end=" ")
            else:
                print("_", end=" ")
                blankCounter = blankCounter + 1
        if blankCounter == 0:
                print("\n\nYou won! The word was \"" + keyWord + "\".")
                break
        print("\nYou have " + str(numGuesses) + " guesses remaining.")
        userInput = input("Guess a letter: ")
        if userInput.upper() in guessedLetters:
            print("You have already guessed that letter.")
        elif userInput.upper() in wordLetters:
            guessedLetters.add(userInput.upper())
        else:
            guessedLetters.add(userInput.upper())
            numGuesses = numGuesses - 1
            if numGuesses == 0:
                print("\nYou lost. The word was \"" + keyWord + "\".")
                break

main()