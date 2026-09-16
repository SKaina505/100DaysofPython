import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a Number between 1 - 100.")
random_number = random.randint(1,100)
difficulty = input("Choose a difficulty, 'easy' or 'hard'.")

live = 0
is_game_over = False

if difficulty == "easy":
    live = 10
    print(f"you have {live} attempts remaining, to guess the Number")
else:
    live = 5
    print(f"you have {live} attempts, to guess the Number")

def game():
    user_guess = int(input("Make a guess"))
    if user_guess == random_number:
        print("You win!")
        global is_game_over
        is_game_over = True
    elif user_guess > random_number:
        global live
        live -= 1
        print("Too High")
        print("Guess Again")
        print(f"you have {live} attempts remaining, to guess the Number")
    elif user_guess < random_number:
        live -= 1
        print("Too Low")
        print("Guess Again")
        print(f"you have {live} attempts remaining, to guess the Number")

while live != 0 and is_game_over == False:
    game()
