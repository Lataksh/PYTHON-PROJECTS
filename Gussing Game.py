import random

number = random.randint(1, 9)
guesses = 0

while guesses < 5:
    user_guess = int(input("Please enter your guessed number!"))
    guesses = guesses + 1
    if user_guess == number:
        print("YAY! You won the game and gussed the correct answer in " + guesses.__str__() + " chances")
        break
    else:
        if user_guess > number:
            print("You guessed it wrong please enter a number less than " + user_guess.__str__())
        else:
            print("You guessed it wrong please enter a number bigger than " + user_guess.__str__())
