from colorama import Fore, Style, Back
import art, random

print(Fore.CYAN + art.logo)
print(Style.BRIGHT + """Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100\n\n""")

random_number = random.randint(1, 100)
life = 0
repeat = True

def game_over(life):
    """
    Check life is 0. If life is 0 game over...
    :param life:
    """
    global repeat
    if life == 0:
        print("Game Over...")
        repeat = False

def compare_user_input(guess):
    """
    Compare random number with user
    :param guess: user_input
    :return: compare result
    """
    global  life, repeat
    if random_number == guess:
        print(f"You got it! The answer was {random_number}\n")
        repeat = False
    elif random_number > guess:
        print("Too low\n")
        life -= 1
        game_over(life)
    else:
        print("Too high\n")
        life -= 1
        game_over(life)

while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if difficulty == 'easy' :
        life = 10
        break
    elif difficulty == 'hard' :
        life = 5
        break
    else:
        print("Invalid input. Type correct difficulty\n")

while repeat:
    print(f"You have << {life} >> attempts remaining to guess the number.")
    guess = int(input("Make a guess : "))

    compare_user_input(guess)