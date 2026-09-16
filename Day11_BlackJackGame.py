import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(x):
    score = sum(x)
    if 11 in x and len(x) == 2:
        score = 0
    if 11 in x and score > 21:
        x.remove(11)
        x.append(1)
    return score

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Your lose"
    elif u_score == 0:
        return "You win"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def play_game():

    print(art.logo)
    user_cards = []
    computer_cards = []
    comp = -1
    user = -1
    game_over = False

    for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not game_over:
        user = calculate_score(user_cards)
        comp = calculate_score(computer_cards)

        if user == 0 or comp == 0 or user > 21:
            game_over = True
        else:
            should_continue = input("Do you want to continue, Type 'y' for Yes and 'n' for No")
            if should_continue == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while comp != 0 and comp < 17:
        computer_cards.append(deal_card())
        comp = calculate_score(computer_cards)

    compare(user, comp)


while input("do you want to play Black Jack, Type 'y' of 'n'") == 'y':
    print("\n" * 20)
    play_game()
