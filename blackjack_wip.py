"""
Blackjack game

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


"""
from turtle import clear

from blackjack_art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_game():
    print(logo)

    def player_game():
        player_score = 0
        player_hand = random.choices(cards, k=2)
        player_score = sum(player_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")

    def dealer_game():
        dealer_score = 0
        dealer_hand = []
        dealer_hand = random.choices(cards, k=1)
        dealer_score = sum(dealer_hand)
        print(f"Computer's first card: {dealer_hand}")

    player_game()
    dealer_game()
    input("Type 'y' to get another card, type 'n' to pass: ")


want_to_play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
if want_to_play == 'y':
    play_game()
else:
    clear()

# dealer_score = 0
# player_score = 0
#
# if dealer_score == player_score:
#     winner = player
# if player_score == 21:
#     winner = player
# if dealer_score == 21:
#     winner = dealer
