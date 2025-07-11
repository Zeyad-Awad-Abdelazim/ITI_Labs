def mark_tasks(tasks_list):
    # retrive incomplete tasks
    incompleteTasks = [task for task in tasks_list if task["status"] == False]
    if not incompleteTasks or len(incompleteTasks) == 0:
        print("All Tasks are completed")
        return
    # view incomplete tasks
    for i, task in enumerate(incompleteTasks):
        print(f"{i+1}. {task['task']}") 

    # get the input task from user and mark it as completed
    try:
        task_number= int(input("Enter the Task Number: "))
        incompleteTasks[task_number-1]["status"] = True

        print(f"The Task [{incompleteTasks[task_number-1]["task"]}] is marked true successfully.")
    except ValueError:
        print("Invalid Input, please enter the number of the task !!")
    except IndexError:
        print("Number of task does not exist")
