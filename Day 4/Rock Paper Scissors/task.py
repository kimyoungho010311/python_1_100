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
#         0      1        2
var = ['rock','paper','scissors']
computer = random.choice(var)
user_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
user = var[user_num]

if computer == 'rock':
    print(rock)
    if user == 'rock':
        print(rock)
        print("Draw")
    elif user == 'paper':
        print(paper)
        print("Win")
    elif user == 'scissors':
        print(scissors)
        print("Loss")
elif computer == 'paper':
    print(paper)
    if user == 'rock':
        print(rock)
        print("Lose")
    elif user == 'paper':
        print(paper)
        print("Draw")
    elif user == 'scissors':
        print(scissors)
        print("Win")
elif computer == 'scissors':
    print(scissors)
    if user == 'rock':
        print(rock)
        print("Win")
    elif user == 'paper':
        print(paper)
        print("Lose")
    elif user == 'scissors':
        print(scissors)
        print("Draw")