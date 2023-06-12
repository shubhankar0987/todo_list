import json


try:
    with open('j_todo_database.json', 'r') as file:
        tasks = json.load(file)
except:
    tasks = []


# To-Do List

main_menu = """
        ----:::: Todo List ::::----

        Choose the below options
    Enter '1' to 'add task'
    Enter '2' to 'view tasks'
    Enter '3' to 'edit tasks'
    Enter '4' to 'delete tasks'
    Enter '5' to 'Close the app'
"""
print(main_menu)
# ui_a = int(input("Enter a number: "))

task_heading = """
        --::Below is Your Tasks::--
"""
# tasks = [1,2,3,4,5]

# Add tasks
def add_task():
    ui = input("Enter a task: ")
    tasks.append(ui)
    print("-----:::Task added successfully:::-----")
    print(main_menu)

# View Task
def view_task():
    print(f"{task_heading}")
    if len(tasks) == 0: 
        print("Sorry you don't have any tasks")
    else:
        for n, v in enumerate(tasks, 0):
            print(f"{n}. {v}")
    print(main_menu)

# Edit Task
def edit_task():
    if ui_a == 3:
        print(f"{task_heading}")
        for n, v in enumerate(tasks, 0):
            print(f"{n}. {v}")
        for n, v in enumerate(tasks, 0):
            ui = int(input("Enter the task number you want to edit: "))
            tasks[ui] = input("Enter the task: ")
            print(tasks)
            break
        print(main_menu)

# Delete Task
def delete_task():
    if ui_a == 4:
        print(f"{task_heading}")
        for n, v in enumerate(tasks):
            print(f"{n}. {v}")
        for n, v in enumerate(tasks):
            ui = int(input("Enter the task number you want to delete: "))
            tasks.remove(tasks[ui])
            print(tasks)
            break
        print(main_menu)


while True:
    ui_a = int(input("Enter a number: "))
    if ui_a == 1:
        add_task()
    elif ui_a == 2:
        view_task()
    elif ui_a == 3:
        edit_task()
    elif ui_a == 4:
        delete_task()
    elif ui_a == 5:
        break
    else:
        print("Enter a valid number")
        print(main_menu)


with open('j_todo_database.json', 'w') as file:
    json.dump(tasks, file)


