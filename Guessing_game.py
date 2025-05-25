
import random

secret_number = random.randint(1,100)

print("welcome to the Number Guessing Game!")
print("i'm thinking of a number between 1 and 100")
print("Try to guess it!\n")

while True:
    guess = input("Enter your guess:")

    if not guess.isdigit():
        print("! please enter  a valid number.\n")
        continue
    guess= int(guess)

    if guess == secret_number:
        print(f"congratulations! you guessed the number {secret_number} correctly!")
        break
    elif guess < secret_number:
        print("Too low. Try again.\n")
    else:
        print("Too high.Try again.\n")

