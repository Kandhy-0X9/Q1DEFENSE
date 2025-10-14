#importing needed modules
import os
import sys

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

    if menuChoice == "add":
        #get the task from the user
        task = input("Enter the task you want to add: ").strip()
        #add the task to the tasks library
        tasks.append(task)
        print(f"Task '{task}' added successfully!")
    
    elif menuChoice == "view":
        #check if there are any tasks
        if not tasks:
            print("No tasks available.")
        else:
            print("Your tasks:")
            for indexx, task in enumerate(tasks, start=1):
                print(f"{indexx}. {task}")

    elif menuChoice == "delete":
        #check if there are any tasks
        if not tasks:
            print("No tasks available to delete.")

           