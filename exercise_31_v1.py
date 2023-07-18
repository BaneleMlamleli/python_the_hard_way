"""
Small math game that generates random numbers for guessing
"""
import random

randomNumber = random.randint(1, 3)
print("Guess a number between 1 and 5. You only have 3 attempts!!")

attempts = 0
correctGuess = False

while (attempts < 3) and (correctGuess != True):
    guessedNumber = int(input("Enter your number: "))
    if (guessedNumber > 5) or (guessedNumber < 1):
        print("You can only guess between 1 and 5")
        # attempts += 1
    else:
        if guessedNumber == randomNumber:
            print(
                f"Well done!! You guessed correctly\nYour number: {guessedNumber}\nGame number: {randomNumber}\nYou had {3-attempts} attempts"
            )
            correctGuess = True
        elif guessedNumber != randomNumber:
            attempts += 1
            print(f"Wrong number :-). Try again! You have {3-attempts} attempts")

print("GAME OVER!! GOOD BYE")
