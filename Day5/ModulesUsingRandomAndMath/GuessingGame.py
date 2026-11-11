import random

number = random.randint(1, 50)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 50.")
print("You have 5 attempts.")

for i in range(5):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You guessed the correct number!")
        break

    elif guess < number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")

else:
    print("Sorry! You have used all 5 attempts.")
    print("The correct number was:", number)