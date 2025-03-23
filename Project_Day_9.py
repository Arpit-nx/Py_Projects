import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("THIS IS A BLIND AUCTION PROGRAM...!!!")

bids = {}

def highest_bidder(bids):
    #highest_bid = max(bid.values())
    #winner = [key for key, value in bid.items() if value == highest_bid]
    #print(f"The winner of this bid is {winner} with the highest bid of {highest_bid}")
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner of this bid is {winner} with the highest bid of {highest_bid}")
        

bidding_done = False
while not bidding_done:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    bids[name] = bid
    cont = input("Are there any bidders left? Type 'yes' or 'no': ")

    if cont == 'no':
        bidding_done = True
        highest_bidder(bids)
    else:
        clear()
