""" Let the user choose the any number between 1 and 100.
The program will check if the generated number is equal to the user's number. 
if number== generated:
    you guessed the number.
elif number > generated:
   to high
elif number < generated:
   to low
else:(if given input is not an integer)
  invalid try again 
loop it till the guess is correct. """
import random
check= True
generated=random.randint(1,100)

while check==True:
    try:
        user_input=int(input("Guess the number between 1 and 100: "))
        if user_input <1 or user_input>100:
            print("Invalid input. Please try again.")
        if user_input==generated:
            print("You guessed the number.")
            check=False
        elif user_input>generated:
            print("Too high.")
        elif user_input<generated:
            print("Too low.")
    except ValueError:
             print("Invalid input. Please try again.")
