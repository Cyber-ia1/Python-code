
# Initialize an empty list to store tasks
To_do = []

# Function to add a task
def add_task(To_do, new_task):    
    To_do.append(new_task)
    print(f"Task '{new_task}' added to the to-do list.")

# Function to view all tasks
def view_tasks(To_do):
    if not To_do:
        print("Your to-do list is empty!")
    else:
        print("Your to-do list:")
        for index, task in enumerate(To_do, start=1):
            print(f"{index}. {task}")

# Function to complete a task
def complete_task(To_do):
    view_tasks(To_do)
    if To_do:
        try:
            task_num = int(input("Enter the task number to mark as complete: "))
            if 1 <= task_num <= len(To_do):
                completed_task = To_do.pop(task_num - 1)
                print(f"Task '{completed_task}' marked as complete and removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main menu function
def todo_menu():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Complete a task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            user_input = input("Enter the task: ")
            add_task(To_do, user_input)
        elif choice == '2':
            view_tasks(To_do)
        elif choice == '3':
            complete_task(To_do)
        elif choice == '4':
            print("Exiting the to-do list manager.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the to-do list menu
todo_menu()

