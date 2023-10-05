import random


class Cards:
    def __init__(self):
        # check index in each item in list for ex: for card in list for letter in card if 'K' == 10  
        self.hand = 0
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
        self.rand_card = random.choice(self.cards)
        self.cards.remove(self.rand_card)
        

        for letter in range(len(self.rand_card)):
            if self.rand_card[letter] == 'A':
                self.rand_card_val = 11
            elif self.rand_card[letter] == '2':
                self.rand_card_val = 2
            elif self.rand_card[letter] == '3':
                self.rand_card_val = 3 
            elif self.rand_card[letter] == '4':
                self.rand_card_val = 4
            elif self.rand_card[letter] == '5':
                self.rand_card_val = 5
            elif self.rand_card[letter] == '6':
                self.rand_card_val = 6
            elif self.rand_card[letter] == '7':
                self.rand_card_val = 7
            elif self.rand_card[letter] == '8':
                self.rand_card_val = 8
            elif self.rand_card[letter] == '9':
                self.rand_card_val = 9
            elif self.rand_card[letter] == '1':
                if self.rand_card[letter+1] == '0':
                    self.rand_card_val = 10
                else:
                    self.rand_card_val = 1
            elif self.rand_card[letter] == 'J':
                self.rand_card_val = 10
            elif self.rand_card[letter] == 'Q':
                self.rand_card_val = 10
            elif self.rand_card[letter] == 'K':
                self.rand_card_val = 10
        return self.rand_card, self.rand_card_val
        
    def start_cards(self):
        for i in range(2):
            self.hand += self.getCards()[1]
            print(f"You currently have a {self.getCards()[0]} in your hand which is worth {self.getCards()[1]}. Your total hand is worth {self.hand}.")