# black jack
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(list=[]):
    # it calculates the score between two cards
    sum = 0
    for card in list:
        if sum(list) > 22 and card == 11:
            list.remove(11)
            list.append(1)
        sum += card
    return sum

user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if user_start == "y":
    score_user = calculate_score(user_cards)
    score_computer = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {score_user}")
    print(f"Computer's first card: {computer_cards[0]}")

new_score_user = score_user
if score_user == 21:
    print(f"You have a black jack. You win!")
elif score_computer == 21:
    print(f"The opponent has a black jack. You lose.")
elif score_user > 21:
    print(f"You went over. You lose.")
elif score_computer > 21:
    print(f"Opponent went over. You win.")
else:
    user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    # if the user wants to draw a card more than 2 times
    while user_choice == "y":
        user_cards.append(deal_card())
        new_score_user = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {new_score_user}")
        print(f"Computer's first card: {computer_cards[0]}")
        if new_score_user > 21:
            print(f"You went over. You lose.")
            break
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ")

print(f"Your final hand: {user_cards}, final score: {new_score_user}")
computer_cards.append(deal_card())
new_score_comp = calculate_score(computer_cards)
while new_score_comp < 17:
    computer_cards.append(deal_card())
print(f"Computer's final hand: {computer_cards}, final score {new_score_comp}")

if new_score_user < 22:
    if new_score_comp == score_user:
        print("It's a draw.")
    elif score_user > new_score_comp:
        print(f"You win!")
    elif new_score_comp > 21:
        print(f"The opponent went over. You win!")
    else:
        print(f"The opponent has a higher score. You lose.")

calculate_score(user_cards)
calculate_score(computer_cards)
