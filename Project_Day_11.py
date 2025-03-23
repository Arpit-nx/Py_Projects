import random as rd
import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


logo = '''
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                         
'''

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

users_cards = []
computers_cards = []

user_sum = 0

#Function to calculate the sum of the cards, handling aces as 1 or 11
def players_deck_sum(hand):
    total = sum(hand)
    ace_count = hand.count(11)
    while total > 21 and ace_count:
        total -= 10
        ace_count -= 1
    return total

#Function to decide the result
def determine_result(user_sum, computer_sum):
    if user_sum > 21:
        return "You lose...!!!"
    elif computer_sum > 21:
        return "You win...!!!"
    elif user_sum == computer_sum:
        return "It's a draw...!!!"
    elif user_sum > computer_sum:
        return "You win 😃"
    else:
        return "You lose...!!!"

#Main game function
def black_jack():
    while True:
        user_input = input("Welcome to the game...Do u wanna strt the game: Type 'y' for yes or 'n' for no: ")
        if user_input == 'y':
            clear()
            print("This is a simple BLACKJACK game...!!!")
            print(logo)

            for i in range(2):
                users_cards.append(rd.choice(deck))
            
            for i in range(2):
                computers_cards.append(rd.choice(deck))
            
            print(f"Your hand is {users_cards} & your total is: {players_deck_sum(users_cards)}")
            print(f"Computers first card is [{computers_cards[0]}]\n")

            #User's turn to draw cards
            should_continue = True
            while should_continue:
                user_choice = input("Do u want an extra card. Type 'y' or 'n': \n")
                if user_choice == 'y':
                    new_card = rd.choice(deck)
                    users_cards.append(new_card)

                    if players_deck_sum(computers_cards) < 17:
                        computers_cards.append(rd.choice(deck))

                    print(f"Your hand is now {users_cards} & your new total is: {players_deck_sum(users_cards)}")
                    print(f"Computers first card is [{computers_cards[0]}]\n")

                    if players_deck_sum(users_cards) > 21:
                        print("You Lose...!!!\n")
                        should_continue = False
                    
                else:
                    print(f"Your final hand is: {users_cards} & your total is: {players_deck_sum(users_cards)}")
                    should_continue = False
            #Computer's turn to draw cards until it reaches at least 17
            while players_deck_sum(computers_cards) < 17:
                computers_cards.append(rd.choice(deck))
            print(f"Computer's final hand is: {computers_cards} & the total is: {players_deck_sum(computers_cards)}\n")  

            #Determine and print the result of the game
            print(determine_result(players_deck_sum(users_cards), players_deck_sum(computers_cards)))

            #Asking to restart the game
            while True:
                restart = input("Do u wanna restart the game: Type 'y' for yes or 'n' for no: ")
                if restart == 'y':
                    break
                elif restart == 'n':
                    print("Thank u for playing...!!!")
                    return
                else:
                    print("Enter a vaild input...!!")

black_jack()
