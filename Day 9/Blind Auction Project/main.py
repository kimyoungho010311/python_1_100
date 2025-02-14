import art
print(art.logo)
bids = {}
continue_bid = True


def find_highest_bidder(bidder_dic):
    highest_bidder = 0
    winner = ''
    for bidder in bidder_dic:
        bid_amount = bidder_dic[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print(f"The winner is {winner} whit ${highest_bidder}")


while continue_bid:
    # TODO-1: Ask the user for input
    bidder_name = input("What is your name? : ")
    price = int(input('What is your bid? : '))
    # TODO-2: Save data into dictionary {name: price}
    bids[bidder_name] = price

    # TODO-4: Compare bids in dictionary

    # TODO-3: Whether if new bids need to be added
    consistent = input("Are there any other bidders? Type 'yes' or 'no' : \n").lower()
    if consistent == 'no':
        continue_bid = False
        find_highest_bidder(bids)
    elif consistent == 'yes':
        print('\n' * 100)
