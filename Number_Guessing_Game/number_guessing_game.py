import random

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

random_number = random.randint(0, 100)

print(f"Psst, the number is {random_number}")

# global variables
easy_level = 10
hard_level = 5


def check_answer(user_guess, random_number):
    if user_guess == random_number:
        return f"You got it. The answer was {random_number}."
    elif user_guess > random_number:
        print("Too high.")
    else:
        print("Too low.")


def difficulty_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_level
    else:
        return hard_level


def guess_number():
    turns = difficulty_level()
    print(f"You have {turns} attempts remaining to guess the number.")
    while turns > 0:
        user_guess = int(input("Make a guess: "))
        check_answer(user_guess, random_number)
        turns -= 1
        if turns == 0:
            return f"You've run out of guesses, you lose."
        elif user_guess != random_number:
            print("Guess again.")
        print(f"You have {turns} attempts remaining to guess the number.")


print(guess_number())
