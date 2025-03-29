import random
print("Welcome to the Number Guessing game!\nYou have 7 attempts to guess the number (from 1-100).\nBegin!")
number = random.randrange(100)
chances = 7
counter = 0
while counter < chances:
    guess = int(input("Enter guess: "))
    counter += 1
    if guess == number and counter == 1:
        print("WOW! You guessed the number on your first try! {number} was correct!")
        break
    elif guess == number:
        print("You did it! {number} is the correct number! You did it in {counter} attempts!")
        break
    elif counter >= chances and guess != number:
        print("Oh no! You are out of attempts! {number} was the answer! Try again!")
        break
    elif guess < number:
        print("Too low! Aim higher!")
    elif guess > number:
        print("Too high! Aim lower!")

