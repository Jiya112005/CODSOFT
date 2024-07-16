def to_do():
    task=[]  #Empty list for storing the tasks
    print("------WELCOME TO TO-DO LIST APP----------------")
    
    total_tasks=int(input("Enter How many tasks you want to add: "))
    
    for i in range(1,total_tasks+1):
        task_name=input(f"Enter task {i} =")
        task.append(task_name)
    
    print(f"Today's tasks are\n{task}")
    
    while True:   #to ask user to perform operations
        operation = int(input("Enter \n1.Add\n2.Update\n3.Delete\n4.View\n5.Exit\n"))
        
        if operation == 1:
            add = input("Enter the task to add:")
            task.append(add)
            print(f"{add} is added to list successfully")
        elif operation == 2:
            updated_val = input("Enter the task you want to update: ")
            if updated_val in task:
                up=input("Enter the new task: ")
                ind = task.index(updated_val) #accessing index of the updating value
                task[ind]=up    #updating new task
                print(f"Updated task: {up}")
            else:
                print("Task is not in the list")
        elif operation == 3:
            del_val=input("Which task you want to delete: ")
            if del_val in task:    
                ind = task.index(del_val)
                del task[ind]
                print(f"Task {del_val} has been deleted.")
            else:
                print("invalid task")
        elif operation == 4:
            print(f"Total tasks are")
            i=1
            for i,t in enumerate(task,start=1):
                print("task:",i,"=",t)
        elif operation == 5:
            print("Closing the application....")
            break
        else:
            print("Invalid input")

to_do()
        