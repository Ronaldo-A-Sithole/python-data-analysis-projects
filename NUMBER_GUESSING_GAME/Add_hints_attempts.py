import random

secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess == secret_number:
        print("Correct! Attempts:", attempts)
        break

    elif guess < secret_number:
        print("Too low")

    else:
        print("Too high")