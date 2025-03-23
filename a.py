import random as rd
import os

# Clear function for console (optional)
def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')


# Logo for the game
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

print("This is a simple BLACKJACK game...!!!")
print(logo)

# Function to calculate the sum of the cards, handling aces as 1 or 11
def calculate_hand_total(hand):
    total = sum(hand)
    ace_count = hand.count(11)
    while total > 21 and ace_count:
        total -= 10
        ace_count -= 1
    return total

# Function to decide the result
def determine_result(user_sum, computer_sum):
    if user_sum > 21:
        return "You lose...!!!"
    elif computer_sum > 21 or user_sum > computer_sum:
        return "You win...!!!"
    elif user_sum == computer_sum:
        return "It's a draw...!!!"
    else:
        return "You lose...!!!"

# Main game function
def black_jack():
    user_input = input("Welcome to the game...Do you want to start the game? Type 'y' for yes or 'n' for no: ")
    
    if user_input.lower() == 'y':
        clear_console()
        
        deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
        users_cards = [rd.choice(deck) for _ in range(2)]
        for card in users_cards:
            deck.remove(card)
            
        computers_cards = [rd.choice(deck) for _ in range(2)]
        for card in computers_cards:
            deck.remove(card)

        print(f"Your hand is {users_cards} & your total is: {calculate_hand_total(users_cards)}")
        print(f"Computer's first card is [{computers_cards[0]}]\n")

        should_continue = True
        while should_continue:
            user_choice = input("Do you want an extra card? Type 'y' for yes or 'n' for no: ").lower()
            if user_choice == 'y':
                new_card = rd.choice(deck)
                users_cards.append(new_card)
                deck.remove(new_card)

                if calculate_hand_total(computers_cards) < 17:
                    new_computer_card = rd.choice(deck)
                    computers_cards.append(new_computer_card)
                    deck.remove(new_computer_card)

                print(f"Your hand is now {users_cards} & your new total is: {calculate_hand_total(users_cards)}")
                print(f"Computer's first card is [{computers_cards[0]}]\n")

                if calculate_hand_total(users_cards) > 21:
                    print("You Lose...!!!")
                    should_continue = False

            else:
                print(f"Your final hand is: {users_cards} & your total is: {calculate_hand_total(users_cards)}")
                should_continue = False

        # Computer's turn to draw cards until it reaches at least 17
        while calculate_hand_total(computers_cards) < 17:
            new_computer_card = rd.choice(deck)
            computers_cards.append(new_computer_card)
            deck.remove(new_computer_card)

        print(f"Computer's final hand is: {computers_cards} & the total is: {calculate_hand_total(computers_cards)}\n")

        # Determine and print the result
        print(determine_result(calculate_hand_total(users_cards), calculate_hand_total(computers_cards)))

        # Ask to restart the game
        restart = input("Do you want to restart the game? Type 'y' for yes or 'n' for no: ").lower()
        if restart == 'y':
            black_jack()
        else:
            print("Thank you for playing...!!!")

black_jack()
