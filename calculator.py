# Input 2 variables, and ask the user what operation they want to and perform the operation in a function which is access by if else statement
def add(x,y):
    sum=x+y
    return sum

def sub(x,y):
    sub=x-y
    return sub

def mul(x,y):
    mul=x+y
    return mul

def div(x,y):
    try:
      div=x/y
      return div
    except ZeroDivisionError:
        print("Invalid denominator please try again.")

def mod(x,y):
    try:
        mod=x%y
        return mod
    except ZeroDivisionError:
        print(ZeroDivisionError)

def power(x,y):
    pow=x**y
    return pow


def value():
 x=int(input("Enter the 1st number:"))
 y=int(input("Enter the 2nd number:"))
 return x,y


def calculator():
    while True:
        x, y = value()

        print("Press 1 for addition")
        print( "Press 2 for subtraction")
        print("Press 3 for multiplication")
        print("Press 4 for division")
        print("Press 5 for Reminder")
        print("Press 6 for Power")
        choice = int(input("Enter your choice for the operation:"))

        if choice == 1:
            print("The addition is:", add(x, y))
        elif choice == 2:
            print("The subtraction is:", sub(x, y))
        elif choice == 3:
            print("The multiplication is:", mul(x, y))
        elif choice == 4:
            print("The division is:", div(x, y))
        elif choice == 5:
            print("The Reminder is:", mod(x, y))
        elif choice == 6:
            print("The Power is:", power(x, y))
        option=input("Do you want to continue or not (y/n):").lower()
        if option=="n":
            print("Thank you for using.")
            break


calculator()


