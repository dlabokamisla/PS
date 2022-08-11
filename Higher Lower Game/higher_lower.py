from game_data import data
# from art import logo
# from art import vs
import random


# not to use global variables, especially with a dictionary

# print(logo)
def compare_people(random_person1, random_person2):
    print(f"Compare A: {random_person1['name']}, {random_person1['description']}, from {random_person1['country']}.")
    # print(vs)
    print(f"Compare B: {random_person2['name']}, {random_person2['description']}, from {random_person2['country']}.")
    print("-----------------------------------------------------------------------------------------------")


def compare_followers(random_person1, random_person2, user_guess, total_score):
    guessed = False
    if user_guess == "A" and random_person1["follower_count"] > random_person2["follower_count"]:
        guessed = True
        print(f"You're right. Current score: {total_score}.")
    elif user_guess == "B" and random_person2["follower_count"] > random_person1["follower_count"]:
        guessed = True
        print(f"You're right. Current score: {total_score}.")
    elif user_guess == "A" and random_person1["follower_count"] < random_person2["follower_count"]:
        print(f"Sorry, that's wrong. Final score: {total_score - 1}.")
    elif user_guess == "B" and random_person2["follower_count"] < random_person1["follower_count"]:
        print(f"Sorry, that's wrong. Final score: {total_score - 1}.")
    return guessed


random_person1 = random.choice(data)

total_score = 1

while True:
    random_person2 = random.choice(data)

    # if random_person1 is equal to random_person2 then the code below will not execute
    # and the loop will start again from the beginning
    if random_person1 == random_person2:
        continue

    compare_people(random_person1, random_person2)
    user_guess = input("Who has more followers? Type 'A' or 'B': ")

    if compare_followers(random_person1, random_person2, user_guess, total_score):
        total_score += 1
        data.remove(random_person1)
        random_person1 = random_person2
    else:
        break
    print("==============================================================================")
