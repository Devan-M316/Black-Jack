import random

between1_4 = eval(input("Please input a number from 1 to 4: "))
dealer_num = random.randint(1, 4)

if dealer_num == between1_4:
    print("Congrats you're the dealer now!")
else:
    print("Darn, you won't be the dealer this round.")

class player:
    def __init__(self):
        # self.__choice = 
        self.hit = False
        self.stay = False
        self.hand = 0

    def setChoice(self):
        if self.hand != 21 and self.hand < 21:
            choice = input("Do you want to hit or stay (h or s)?")
            if choice.lower() == "h":#choice is to hit
                hit()
            
            else:#choice is to stay/stand
                stay()
"""    
    def hit(self):
        
            



    def stay(self):
        """