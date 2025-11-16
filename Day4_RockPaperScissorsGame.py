import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock,paper,scissors]
userchoice = input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors\n")

if userchoice == "0":
    print(rock)
    computerchoice = random.choice(game)
    if computerchoice == game[0]:
        print("Computer choose\n")
        print(rock)
        print("A tie.\n")
    elif computerchoice == game[1]:
        print("Computer choose\n")
        print(paper)
        print("I win.\n")
    elif computerchoice == game[2]:
        print("Computer choose\n")
        print(scissors)
        print("You win\n")
elif userchoice == "1":
    print(paper)
    computerchoice = random.choice(game)
    if computerchoice == game[0]:
        print("Computer choose\n")
        print(rock)
        print("You win.\n")
    elif computerchoice == game[1]:
        print("Computer choose\n")
        print(paper)
        print("A tie.\n")
    elif computerchoice == game[2]:
        print("Computer choose\n")
        print(scissors)
        print("I win\n")
elif userchoice == "2":
    print(scissors)
    #game = [rock, paper, scissors]
    computerchoice = random.choice(game)
    if computerchoice == game[0]:
        print("Computer choose\n")
        print(rock)
        print("I win.\n")
    elif computerchoice == game[1]:
        print("Computer choose\n")
        print(paper)
        print("You win.\n")
    elif computerchoice == game[2]:
        print("Computer choose\n")
        print(scissors)
        print("A tie\n")
else:
    print("Wrong input, Kindly follow the instruction above")
