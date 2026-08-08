""" Ask user if he/she wants to roll the dice.
If yes :
   Roll the dice ( make sure it is random number between 1 and 6), and show the result. 
If no:
   Exit the game with a goodbbye message. """
import random
n=0
while n<=5:
    choice=input("Do you want to roll the dice? (y/n): ")
    check=True

    if choice.lower()=='y':
        dice_roll1=random.randint(1,6)
        dice_roll2=random.randint(1,6)
        print(f"Values: ({dice_roll1}, {dice_roll2})")
    elif choice.lower()=='n':
        print("Goodbye!")
    else:
       print("Invalid input. Please try again")
    n+=1
