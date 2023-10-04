import random as random
import turtle as t

# wn = t.Screen()
# 540 x 360
from player import player
"""t.bgpic("green_felt_bg.gif")

card_back = t.Turtle()
wn.addshape('card_back.gif')

card_back.shape('card_back.gif')"""

class Cards:
    def __init__(self):
        # check index in each item in list for ex: for card in list for letter in card if 'K' == 10  
        self.cards = [
        "card_clubs_A.gif",
        "card_clubs_02.gif",
        "card_clubs_03.gif",
        "card_clubs_04.gif",
        "card_clubs_05.gif",
        "card_clubs_06.gif",
        "card_clubs_07.gif",
        "card_clubs_08.gif",
        "card_clubs_09.gif",
        "card_clubs_10.gif",
        "card_clubs_J.gif",
        "card_clubs_Q.gif",
        "card_clubs_K.gif",
        "card_diamonds_A.gif",
        "card_diamonds_02.gif",
        "card_diamonds_03.gif",
        "card_diamonds_04.gif",
        "card_diamonds_05.gif",
        "card_diamonds_06.gif",
        "card_diamonds_07.gif",
        "card_diamonds_08.gif",
        "card_diamonds_09.gif",
        "card_diamonds_10.gif",
        "card_diamonds_J.gif",
        "card_diamonds_Q.gif",
        "card_diamonds_K.gif",
        "card_hearts_A.gif",
        "card_hearts_02.gif",
        "card_hearts_03.gif",
        "card_hearts_04.gif",
        "card_hearts_05.gif",
        "card_hearts_06.gif",
        "card_hearts_07.gif",
        "card_hearts_08.gif",
        "card_hearts_09.gif",
        "card_hearts_10.gif",
        "card_hearts_J.gif",
        "card_hearts_Q.gif",
        "card_hearts_K.gif",
        "card_spades_A.gif",
        "card_spades_02.gif",
        "card_spades_03.gif",
        "card_spades_04.gif",
        "card_spades_05.gif",
        "card_spades_06.gif",
        "card_spades_07.gif",
        "card_spades_08.gif",
        "card_spades_09.gif",
        "card_spades_10.gif",
        "card_spades_J.gif",
        "card_spades_Q.gif",
        "card_spades_K.gif"]
        
    def getCards(self):
        for cards in range(len(self.cards)):
            rand_card = self.cards.pop(random.randint(0,51))
            for letter in range(len(rand_card)):
                if rand_card[letter] == 'A':
                    rand_card_val = 11
                elif rand_card[letter] == '2':
                    rand_card_val = 2
                elif rand_card[letter] == '3':
                    rand_card_val = 3
                elif rand_card[letter] == '4':
                    rand_card_val = 4
                elif rand_card[letter] == '5':
                    rand_card_val = 5
                elif rand_card[letter] == '6':
                    rand_card_val = 6
                elif rand_card[letter] == '7':
                    rand_card_val = 7
                elif rand_card[letter] == '8':
                    rand_card_val = 8
                elif rand_card[letter] == '9':
                    rand_card_val = 9
                elif rand_card[letter] == '10':
                    rand_card_val = 10
                elif rand_card[letter] == 'J':
                    rand_card_val = 10
                elif rand_card[letter] == 'Q':
                    rand_card_val = 10
                elif rand_card[letter] == 'K':
                    rand_card_val = 10


        return rand_card, rand_card_val

