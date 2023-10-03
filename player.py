import random

between1_4 = eval(input("Input a number from 1 to 4"))
dealer_num = random.randint(1, 4)
print(dealer_num)
if dealer_num == between1_4:
    print("Congrats you're the dealer now!")
else:
    print("Darn, you won't be the dealer this round.")
"""
class player:
    def __init__(self):
        self.__choice =  
        self.__hit =
        self.__stay = 

    def getChoice(self):
        return self.__choice
        
"""