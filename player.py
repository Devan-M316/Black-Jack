import random
from cards import Cards

class Player:
    def __init__(self):
        self.hit = Cards()
        self.stay = False
        # self.hand = 0

    def dealer(self):
        between1_4 = eval(input("Please input a number from 1 to 4: "))
        dealer_num = random.randint(1, 4)
        
        if dealer_num == between1_4:
            print("Congrats you're the dealer now!")
        else:
            print("Darn, you won't be the dealer this round.")


    def setChoice(self):
        if self.hand != 21 and self.hand < 21:
            choice = input("Do you want to hit or stay (h or s)?")
            if choice.lower() == "h":#choice is to hit
                print(f"Your card was a {self.hit.getCards()[0]}, so it was worth {self.hit.getCards()[1]}.")
                self.hand += self.hit.getCards()[1]
                if self.hit.hand > 21:
                    print("You have busted")
                elif self.hit.hand == 21:
                    print("You have gotten 21 and won")
                                
            else:#choice is to stay/stand
                print("imagine staying loser")


# class Dealer:
#     def __init__(self):

"""    
    def hit(self):
        
            



    def stay(self):
        """