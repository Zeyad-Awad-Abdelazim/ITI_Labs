def add_task(tasks_list):
    # get input task
    task = input("Enter Your Task: ")

    # define task status
    task_info = {
        "task": task,
        "status": False,
        "note": "nth"
    }

    # add task to the tasks list
    if task != "":
        tasks_list.append(task_info)
        print("Task added Successfuly")
    else:
        print("Task is not added")