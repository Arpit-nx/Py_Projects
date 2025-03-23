import random as rd
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

logo = '''
 ░░      ░░░  ░░░░  ░░        ░░░      ░░░░      ░░░░░░░░░        ░░  ░░░░  ░░        ░░░░░░░░   ░░░  ░░  ░░░░  ░░  ░░░░  ░░       ░░░        ░░       ░░
▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒  ▒▒  ▒▒▒▒  ▒▒   ▒▒   ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒
▓  ▓▓▓   ▓▓  ▓▓▓▓  ▓▓      ▓▓▓▓▓      ▓▓▓▓      ▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓        ▓▓      ▓▓▓▓▓▓▓▓▓▓  ▓  ▓  ▓▓  ▓▓▓▓  ▓▓        ▓▓       ▓▓▓      ▓▓▓▓       ▓▓
█  ████  ██  ████  ██  ██████████████  ████████  ███████████  █████  ████  ██  ██████████████  ██    ██  ████  ██  █  █  ██  ████  ██  ████████  ███  ██
██      ████      ███        ███      ████      ████████████  █████  ████  ██        ████████  ███   ███      ███  ████  ██       ███        ██  ████  █
'''

def mode_of_game():

    Choice = input("ON WHICH LEVEL U WANNA PLAY...TYPE EASY OR DIFFICULT: ").lower()
    if Choice == 'easy':
       Guesses = 10
       main_game(Guesses)
    
    if Choice == 'difficult':
      Guesses = 5
      main_game(Guesses)

def main_game(Guesses):
    print(logo)
    print("Start..!!!\n")
    
    Computers_guess = rd.randint(0,101)
    print("The computer has chosen a number between 1 and 100\n")

    while Guesses != 0:
        print(f"You have {Guesses} attempts remaining")
        users_guess = int(input("Guess a number between 0 and 100: "))

        if users_guess > Computers_guess:
            print("Too high!!!")
        elif users_guess < Computers_guess:
            print("Too low!!!")
        elif users_guess == Computers_guess:
            print("You found it...You won!!!")
            break
        else:
            print("Enter a valid input inbetween 1 to 100!!")

        Guesses -= 1
        if Guesses == 0:
            print("You are out of attempts...You lost!!!")
            print(f"Computer's guess was {Computers_guess}")

    Restart = input("Do u wanna restart the game? Type 'y' for yes  or 'n' for no: ").lower()
    if Restart == 'y':
        clear()
        mode_of_game()
    else:
        print("Thank you for playing...!!!")
        exit

mode_of_game()
