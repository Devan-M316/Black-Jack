# ideas for code starting from scratch

import random

"""
class Card():
    def __init__(self):
        self.suits = ["spades","clubs","diamonds","hearts"]
        self.card_value = {"ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", 'king'}

    def getCardValue(self):
        self.cardVal = random.choice(self.card_value)
        self.suit = random.choice(self.suits)
        print(f"{self.cardVal} of {self.suit}")
for suit in suits:
        for card in card_value:
"""

suits = ["spades","clubs","diamonds","hearts"]
cardValueList = {"ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", 'king'}

def getCardVal():
    cardVal = random.choice(cardValueList)
    suit = random.choice(suits)
    print(f"{cardVal} of {suit}")

def deal_cards():
    global cardValueList
    cardValueList, cardSuit = random.choice(cardValueList), random.choice(suits)
    print(cardValueList, 'of', cardSuit)
    return cardValueList, cardSuit

def getCardVals(card):
    if cardValueList == 'ace' or card == 'ace':
        cardVal = eval(input('Do you want ace to be 1 or 11: '))
    elif cardValueList == '2' or card == '2':
        cardVal = 2
    elif cardValueList == '3' or card == '3':
        cardVal = 3
    elif cardValueList == '4' or card == '4':
        cardVal = 4
    elif cardValueList == '5' or card == '5':
        cardVal = 5
    elif cardValueList == '6' or card == '6':
        cardVal = 6
    elif cardValueList == '7' or card == '7':
        cardVal = 7
    elif cardValueList == '8' or card == '8':
        cardVal = 8
    elif cardValueList == '9' or card == '9':
        cardVal = 9
    elif cardValueList == '10' or cardValueList == 'J' or cardValueList == 'Q' or cardValueList == 'K' or card == '10' or card == 'J' or card == 'Q' or card == 'K':
        cardVal = 10
    return cardVal

def evaluateCards(card1, card2):
    while True:
        cardTotal = card1 + card2 + extraCardVal
        extraCardVal = 0
        if cardTotal == 21:
            print('You win!')
            break
        elif cardTotal > 21:
            print('Big loser just like Mason Skylar Percival ')
            break
        else:
            hitOrStay = input('Would you like to hit (y/n)? ')
            if hitOrStay.lower() == 'y' or hitOrStay.lower() == 'yes':
                extraCard = deal_cards()
                extraCardVal = getCardVal(extraCard)
                continue
            else:
                break
            

