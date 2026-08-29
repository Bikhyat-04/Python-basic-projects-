""" Shopping list manager 
things to add in this manager workspace:
-> Add items to the shopping list with their quantity
-> View items in the shopping list with their quantity
-> Remove items that is choosen from the shopping list
->Change the quantity of the item in the shopping list"""

list=[]

def add_item():
     item=input('Enter the item you want to add:').lower()
     value=(input("Enter the quantity of item you want to add:"))
     list.append({"item":item,"quantity":value})
     print("Item added\n")

def view_item():
    if len(list)==0:
        print("Empty list\n")

    else:    
       for i in range(len(list)):
            print(f"{i+1}. Item:{list[i]['item']} -- Quantity:{list[i]['quantity']}\n")
                    
def change_item():
    if len(list)==0:
        print("List is empty\n") 

    else:
        index=int(input("Enter the item number:"))
        quantity=input("enter the new quantity:")
        for i in range (0,len(list)):
            if (i+1)==index:
                list[i]['quantity']=quantity
        print("value successfully changed\n")


def rem_item():
    if len(list)==0:
        print("List is empty\n")

    else:
        index=int(input("Enter the item number you want to remove:"))
        list.pop(index-1)
        print("item successfully removed\n")



def main(): 

    while True:

        print(".......Main Menu........")
        print("Press 1 to add item in the shopping list.")
        print("Press 2 to view item in the shopping list")
        print("Press 3 to change the quantity of choosen item in the shopping list")
        print("Press 4 to remove a item in the shopping list")
        print("Press 5 to exit the application")

        choice=int(input("Enter your choice:"))
        print("\n")

        if choice==1:
            add_item()

        elif choice==2:
            view_item()

        elif choice==3:
            change_item()

        elif choice==4:
            rem_item()

        elif choice==5:
            print("Exiting the application")
            exit()

        else:
            print("Invalid choice try again")


main()