"""Generate random rock, paper or scissors and ask the user to guess his/her choice.
If user choose rock and computer choose scissors, user wins.
elif user choose paper and computer choose rock, user wins.
elif user choose scissors and computer choose paper, user wins.
elif user choose rock and computer choose paper, computer wins.
elif user choose paper and computer choose scissors, computer wins.
elif user choose scissors and computer choose rock, computer wins.
else invalid value try again.
after every result ask user if he/she wants to continue or not. if not exit"""

import random
rn=('r','p','s')

def choice():
    while True:
        user_choicee=input("Enter your choice(r/p/s):").lower()
        if user_choicee in rn:
          return user_choicee 
        else:
          print("Invalid input. Please try again.")


def displaying_choice(user_choice,computer_choice):
    print("You choose:",user_choice)
    print("computer choose:",computer_choice)

def determin_winner(user_choice,computer_choice):
                 if user_choice not in ['r','p','s']:
                     print("Invalid input. Please try again.")
                 if user_choice ==computer_choice:
                     print("It's a tie")
                 elif((user_choice=="r" and computer_choice=="s") or (user_choice=='p' and computer_choice=='r')or ( user_choice =='s' and computer_choice=="p")):
                     print("You win")
                 else:
                     print("computer wins")


def play_game():         
 while True:
     user_choice=choice() 
     computer_choice=random.choice(rn)
     displaying_choice(user_choice,computer_choice)
     determin_winner(user_choice,computer_choice)
     option=input("Do you want to continue? (y/n): ").lower()
     if option=='n':
          print("Thank you for playing.")
          break
     
play_game() 

    
   

