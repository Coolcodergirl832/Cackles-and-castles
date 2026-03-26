import CAC
from CAC import the_first_game
from CAC_overclocked import the_second_game
print("main_menue")
print("what installment of the series do you want to play?")
game = input("1, 2, or 3? ")
if game == "1":
    the_first_game()
if game == "2":
    the_second_game()
if game == "3":
    print("the third game is currently in development, check back later!")