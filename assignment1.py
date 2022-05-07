import random

num = random.randint(1, 100)
guess = None

while guess != num:
    guess = input("guess a number between 1 and 100: ")
    guess = int(guess)

    if guess > num:
        print("Guess lower")
        
    elif guess < num:
        print("Guess higher")
        
    else:
        print("Number guessed is correct!!!")
