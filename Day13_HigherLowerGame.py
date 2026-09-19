import random
import art
import game_data
print(art.logo)


def name(x):
    answer = game_data.data[x]["name"]
    return answer

def description(x):
    answer = game_data.data[x]["description"]
    return answer

def country(x):
    answer = game_data.data[x]["country"]
    return answer

def follow(x):
    answer = game_data.data[x]["follower_count"]
    return answer

def compare(x,y):
    if x > y:
        return "A"
    else:
        return "B"


is_game_over = False
score = 0
num1 = random.randint(0, 49)

while not is_game_over:

    num2 = random.randint(0, 49)

    while num2 == num1:
        num2 = random.randint(0, 49)

    A1 = follow(num1)
    B2 = follow(num2)


    print(f"Compare A: {name(num1)}, a {description(num1)}, from {country(num1)}.")
    print(art.vs)

    print(f"Against B: {name(num2)}, a {description(num2)}, from {country(num2)}.")

    predict = input("Who has more followers 'A' or 'B': ")

    greater = compare(A1, B2)

    if predict == greater:
        score += 1
        print(f"You are right! Current score: {score}")
        num1 = num2
    else:
        is_game_over = True
        print(f"Sorry, that's wrong. Your Final score: {score}")
