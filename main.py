from random import randint

#Function to check user's guess against actual answer
def check_answer(guess, answer):
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")
    else:
        print(f"You got it! The answer was {answer}")

        

print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100")

answer = randint(1,100)

guess = int(input("Make a guess: "))
 