def view_tasks(tasks_lists):
    if not tasks_lists or len(tasks_lists) == 0:
        print("No Tasks added yet !")
        return 
    
    for i, task in enumerate(tasks_lists):
        mark = "✅" if task["status"] else "❌"
        print(f"{i+1}. {task['task']}. {mark}")