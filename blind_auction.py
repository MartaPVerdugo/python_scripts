from art import logo
import os

print(logo)

bids = {}


def bidding(bidder_name, bid_value):
    bids[bidder_name] = bid_value


def find_winner():
    highest_bid = 0
    for bidder_name, bid_value in bids.items():
        if bid_value > highest_bid:
            highest_bid = bids[bidder_name]
    if bid_value == highest_bid:
        print(f"The winner is {bidder_name} with {highest_bid}$.")


def clear():
    os.system('cls')  # on Windows System


continue_bidding = True

while continue_bidding:
    name = input("What's your name? ")
    bid = int(input("What's your bid? "))
    bidding(bidder_name=name, bid_value=bid)
    answer = input("Type 'yes' if you want add more bids. Otherwise type 'no'.\n")
    if answer == "yes":
        clear() # this will not work in pycharm. The IDLE shell is not the same.
    if answer == "no":
        continue_bidding = False

find_winner()
