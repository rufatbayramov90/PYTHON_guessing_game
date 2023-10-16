from random import randint

easy_level_turns = 10
hard_level_turns = 5

#Function to check user's guess against actual answer
def check_answer(guess, answer):
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")
    else:
        print(f"You got it! The answer was {answer}")


#Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty.Type 'easy' or 'hard': ") 
    if level == "easy":
        return easy_level_turns
    else:
        return  hard_level_turns


print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100")
answer = randint(1,100)
print(f"The correct answer is {answer}")
turns = set_difficulty()
print(f"You have {turns} attempts to guess the number")
guess = int(input("Make a guess: "))

check_answer(guess)

 