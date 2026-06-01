tasks=[]
try:
    with open("tasks.txt","r") as f:
        for t in f:
            task,completed=t.strip().split("-")
            tasks.append({"task":task,"completed":completed==True})
except FileNotFoundError:
    tasks=[]
while (True):
    print("\nTodo List App\n")
    print("1.Add Task\n" \
    "2.Delete Task\n" \
    "3.Update Task\n" \
    "4.List Task with status\n" \
    "5.Exit\n")

    ch=int(input("Enter your choice: "))
    

    if ch==5:
        print("Exiting...\n")
        break
    elif ch==1:
        task_name=input("Enter task to add: ")
        print(f"{task_name} added to todo list")
        task={"task":task_name,"completed":False}
        tasks.append(task)
        
        with open("tasks.txt","w") as f:
            for t in tasks:
                f.write(f"{t['task']}-{t['completed']}\n")

    elif ch==2:
        for i,t in enumerate(tasks):
            print(f"{i+1}.{t['task']}")

        dele=int(input("Enter task id to delete: "))
        tasks.pop(dele-1)

        with open("tasks.txt","w") as f:
            for t in tasks:
                f.write(f"{t['task']}-{t['completed']}\n")
        print("\nTask deleted successfully")
    

    elif ch==3:
        for i,t in enumerate(tasks):
            print(f"{i+1}.{t['task']}")
        upd=int(input("Enter task id to marked as completed: "))

        for i,t in enumerate(tasks):
            if i==(upd-1):
                t["completed"]=True
            print("\nTask marked as completed")



    elif ch==4:
            for t in tasks:
                if t["completed"]:
                    print(f"[X] {t['task']}")
                else:
                    print(f"[ ] {t['task']}")
