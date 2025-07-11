import Add_Task, View_Tasks, Mark_Tasks

msg = """ 
###############################################
##### CHOOSE ONE OF THE FOLLOWING: ############
###############################################
#### 1. Add Task               ################
#### 2. View Tasks             ################
#### 3. Mark Task as Completed ################
#### 4. Quit                   ################
############################################### 
    """
tasks = [
    {
        "task": "study python",
        "status": False,
        "note": "nth"
    },
    {
        "task": "gym workout",
        "status": False,
        "note": "nth"
    },
    {
        "task": "complete the project",
        "status": False,
        "note": "nth"
    },
    {
        "task": "ay 7aga",
        "status": False,
        "note": "nth"
    },
]

while True:
    print(msg)
    choice = input("Enter your choice: ")

    if choice == "1":
        Add_Task.add_task(tasks)
    elif choice == "2":
        View_Tasks.view_tasks(tasks)
    elif choice == "3":
        Mark_Tasks.mark_tasks(tasks)
    elif choice == "4":
        break
    else:
        print("Invalid Choice... ")