#needed modules
import os
import sys
import time
import datetime
from datetime import datetime
import msvcrt 

# Constants
TASK_FILE = "tasks.txt"
tasks = []

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                if line.strip():
                    timestamp, task = line.strip().split(" | ", 1)
                    tasks.append({"task": task, "timestamp": timestamp})

# Save tasks to file
def save_tasks():
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['timestamp']} | {task['task']}\n")

# Add a task
def add_task():
    task_text = input("\nEnter the task you want to add: ").strip()
    if task_text:
        timestamp = datetime.now().strftime("%Y-%m-%d , %H:%M")
        tasks.append({"task": task_text, "timestamp": timestamp})
        print(f"\n Task '{task_text}' added successfully!\n")
        save_tasks()
    else:
        print(" Task cannot be empty.")

# View tasks
def view_tasks():
    if not tasks:
        print("\n No tasks available.")
    else:
        print("\n Your tasks:")
        sorted_tasks = sorted(tasks, key=lambda x: x["timestamp"])
        for index, task in enumerate(sorted_tasks, start=1):
            print(f"{index}. {task['task']} (added: {task['timestamp']})")

# Delete a task
def delete_task():
    if not tasks:
        print("\n No tasks to delete.")
        return

    print("\n Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['task']} (added: {task['timestamp']})")

    try:
        task_number = int(input("\nEnter the number of the task to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            removed = tasks.pop(task_number)
            print(f"\n Task '{removed['task']}' removed successfully!\n")
            save_tasks()
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")


##################################################################################################
# Main loop
#this is what the user will see when they run the program
def main():
    print(" Welcome to your Task Manager!")
    load_tasks()

    while True:
        print("\n Menu:\n")
        print("1. Add a task     → add")
        print("2. View tasks     → view")
        print("3. Delete a task  → delete")
        print("4. Exit           → exit")
        print("4. Show Time      → time")

        choice = input("\nWhat would you like to do? ").strip().lower()
        # Handle user choice

        #add task
        if choice == "add":
            add_task()
           
        #view tasks
        elif choice == "view":
            view_tasks()

        #remove task
        elif choice == "delete":
            delete_task()
            
        #exit program
        elif choice == "exit":
            save_tasks()
            print("\n Saving tasks...")
            time.sleep(1)
            print(" Goodbye!")
            sys.exit()

        #invalid input
        else:
            print(" Invalid choice. Please type: add, view, delete, or exit.")
# Run the main function
if __name__ == "__main__":
    main()
