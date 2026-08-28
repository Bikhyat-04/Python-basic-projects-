#function that the to do list does:
#Add a task
# view a task
# delete a task
# mark the task done
todo=[]
def add_task():
   task=input("Enter your task:")  
   todo.append({"task":task, 
                "status": "pending"})
   print("New task added succesfully\n")

def view_task():  
   if len(todo)==0:
      print("No items in list")
   else:
      for index,task in enumerate(todo,1):
         print(f"{index}:{task['task']}-{task['status']}\n")

def rem_task():
    
   if len(todo)==0:
      print("No items in list")
   else:
      value=int(input("Which task number you want to remove:"))-1 
      if value>=0 and value<len(todo):
            removed=todo.pop(value)
            print(f"task removed:",removed,"\n")
      else:
         print("invalid task number")


def mark_task():
    
   if len(todo)==0:
      print("No items in list")
   else:
      value=int(input("Which task status you want to change:"))-1 
      if value>=0 and value<len(todo):
            todo[value]["status"]="done"
            print(f"{todo[value]['task']},has been marked as done\n")
      else:
         print("invalid task number")
def main():
   while True:

        print("Main Menu")
        print("Press 1 to add task")
        print("Press 2 to view task")
        print("Press 3 to remove task")
        print("Press 4 to mark the task done")
        print("Press 5 to exit\n")


        choice=int(input("Enter your choice:"))
        print("\n")
        if choice==1:
           add_task()
        elif choice==2:
           view_task()
        elif choice==3:
           rem_task()
        elif choice==4:
           mark_task()
        elif choice==5:
           print("Closing the application")
           exit()
        
        else:
           print("Invalid choice")

main()