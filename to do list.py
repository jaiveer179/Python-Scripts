def task():
    task = [] # create an empty list to store tasks 
    print("Welcome to te To-Do list app!")

    total_tasks = int(input("How man tasks would you like to add?")) # ask the user how many tasks they would like to add
    for i in range  (1, total_tasks + 1):
        task_name = input (f" enter task {i}:")# ask the user to enter the task
        task.append(task_name)

        print(f"today's tasks are:\n {task}") # print the tasks entered by user 

        while True:
            operation = int(input("Enter 1 to add a task,\n 2 to delete a task,\n 3 to view all tasks, 4 to exit "))
            if operation == 1:
                add  = input("Enter the task you want to add =")
                task.append(add)
                print(f"Task{add} has been successfully added....")

            elif operation == 2:
                updated_val = input ("Enter  the task you want to update = ")
                if updated_val in task:
                    up = input("Enter the new task = ")
                    ind = task.index(updated_val)#2
                task [ind] = up
                print(f"updated task{up}")

