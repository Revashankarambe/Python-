user = input("Snake/water/Gun :").lower()
import random
choices = ["snake" , "water" , "gun"]
computer = random.choice(choices)
if user == computer:
    print("Draw")

elif(
(user == "snake" and computer == "water")or 
   (user == "water" and computer == "gun")or
   (user == "gun" and computer == "snake")
):
   print("you win")

else:
    print("computer wins")   
