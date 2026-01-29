import random
import art
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(card_list):
    if sum(card_list)==21 and len(card_list)==2:
        return 0
    if 11 in card_list and sum(card_list)>21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 😒"
    elif c_score ==0:
        return "Lose, Opponent has a Blackjack 😱"
    elif u_score ==0:
        return "You won with Blackjack 😎"
    elif u_score > 21:
        return "Lose, You went over 😱"
    elif c_score > 21:
        return "You win, Opponent went over 😊"
    elif  u_score > c_score:
        return "You win 😍"
    else:
        return f"You lost 😑"

print("Welcome to the Black Jack game.")
def play():
    print(art.logo)
    user_cards = []
    computer_cards =[]
    computer_score = -1
    user_score = -1
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards are :{user_cards}, Current score is {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")

        if user_score == 0 or computer_score ==0 or user_score >21:
            is_game_over = True
        else:
            user_choice = input('Type "y" to take another card, "n" to pass :').lower()
            if user_choice == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand : {user_cards} and final score: {user_score}")
    print(f"Computer's final hand : {computer_cards} and final score: {computer_score}")
    print(compare(user_score, computer_score))

should_continue=True
while should_continue:
    play()
    end_game=input("Do You want to continue? : y or n:")
    if end_game == "n":
        print("Hope you enjoyed the game! See Ya!! 🫡 ")
        should_continue=False
    else:
        print("\n" * 100)






