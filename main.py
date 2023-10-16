from random import randint

easy_level_turns = 10
hard_level_turns = 5

turns = 0
#Function to check user's guess against actual answer
def check_answer(guess, answer,turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1 
    else:
        print(f"You got it! The answer was {answer}")


#Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty.Type 'easy' or 'hard': ") 
    if level == "easy":
        return easy_level_turns
    else:
        return  hard_level_turns

def game():
    print("Welcome to the Number Guessing Game")
    print("I am thinking of a number between 1 and 100")
    answer = randint(1,100)
    print(f"The correct answer is {answer}")

    turns = set_difficulty()
    while guess != answer:
        print(f"You have {turns} attempts to guess the number")

        guess = 0
        while guess != answer:
            guess = int(input("Make a guess: "))
            turns = check_answer(guess,answer,turns)
            if turns == 0:
                print("You have run out of guesses, you lose")
                return
            elif guess != answer:
                print("Guess again")



game()

 