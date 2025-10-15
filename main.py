#importing needed modules
import os
import sys
import time

#welcome the user
print("Welcome to your tasks manager!")

#make a while loop to keep the program running until the user decides to exit
while True:
    #make a tasks library
    tasks = []
    #display the menu options
    print("\nMenu:\n")
    print("1. To add a task : add")
    print("2. To view tasks : view")
    print("3. To delete a task : delete")
    print("4. To exit : exit")

    #get the user's choice
    menuChoice = input("\nWhat would you like to do? ").strip().lower()

    #allow the user to add a task 
    if menuChoice == "add":
        #get the task from the user
        addTask = input("\nEnter the task you want to add: ")
        #add the task to the tasks library
        print(f"\nTask '{addTask}'added successfully!\n")
        tasks.append(addTask)
    
    #show tasks available for the user
    elif menuChoice == "view":
        #check if there are any tasks
        if not tasks:
            print("\nNo tasks available to view.")
        else:
            print("\nYour tasks:")
            tasks.sort()
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    #Allowing the user to remove tasks in the library
    elif menuChoice == "delete":
        #check if there are any tasks
        if not tasks:
            print("\nNo tasks available to delete.")
        else:
            removeTask = input("\nWhat task would you like to remove: ")
            #remove users choice
            print(removeTask, "was removed successfully.")
            tasks.remove(removeTask)

    #quit the program but save the list
    elif menuChoice == "exit":
        os.system('cls||clear')
        print("Exiting the program")
        time.sleep(2)
        sys.exit()
        
    #show error masage in user types something else
    else:
        print("Sorry, You Have to type on of the choices\n")  