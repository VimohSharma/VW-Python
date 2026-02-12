#number guessing game
import random
secret_num=random.randint(1,100)
life=7

while life>0:
    guess=int(input("Make a guess: "))

    if guess>secret_num:
        print("Too high! Try a smaller number.")
    elif guess<secret_num:
        print("Too low! Try a larger number.")
    else:
        print("Congratulations, you have guessed the secret number!!!!")
        break
    guess-=1
    print(f"Lives Left: {guess}")

    if(guess==0):
        print(f"You lost! the secret number was {secret_num}")
