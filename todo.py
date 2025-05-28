import random,os,string,math

os.system("cls")

title = []
desc = []
tasks = []
donetasks = []
statusn = []

def CheckLists(x,y):
    if os.path.exists(x + ".txt"):
        with open((x + ".txt"), "r") as checkk:
            y[:] = checkk.read().splitlines()

def CheckTasks(x, y):
    if os.path.exists(x + ".txt"):
        with open(x + ".txt", "r") as readd:
            content = readd.read().strip()
        y.clear()
        if content:
            groups = content.split("\n\n")
            for group in groups:
                if group:
                    task_list = group.split("\n")
                    y.append(task_list)
                else:
                    y.append([])
        else:
            y.append([])

def AddListElements(x,y):
    with open((x + ".txt"), "w") as adderr:
        adderr.write("\n".join(y) + "\n")

def AddTasks(x,y):
    with open((x + ".txt"), "w") as adderr:
        for adderr_list in y:
            if adderr_list:
                adderr.write("\n".join(adderr_list))
                adderr.write("\n\n")
            else:
                adderr.write("\n\n")

def RemoveFile(x):
    if os.path.exists(x + ".txt"):
        os.remove(x + ".txt")

CheckLists("titles", title)
CheckLists("descriptions", desc)
CheckLists("statusn", statusn)
CheckTasks("tasks", tasks)
CheckTasks("dtasks", donetasks)

def PrintActions():
    print("Actions : ")
    print("    1) Create list")
    print("    2) Add Todo")
    print("    3) Check Todo's")
    print("    4) Complete Task")
    print("    5) Configure List")
    print("    6) Save Todo's")
    print("    7) Delete Saves")
    print("    8) Export to Txt")
    print("    9) Actions")

PrintActions()

while True:
    action = input("\nAction: ")
    
    match action:
        case "1":
            title.append(input("\nTitle: "))
            desc.append(input("Description: "))
            tasks.append([])
            donetasks.append([])
            statusn.append("Incomplete")
            print("List Created!")

        case "2":
            if len(title) == 0:
                print("\nNo lists yet! create a list.")
            else:
                print("\nLists : ")
                for lcheck in range(0,(len(title))):
                    print(f"    - {title[lcheck]} ({lcheck})")
                lnum = int(input("\nList Number: "))
                todo = input("Task to add: ")
                tasks[lnum].append(todo)
                taskgroup = tasks[lnum]
                if(len(donetasks[lnum]) != 0 and len(taskgroup) == 0):
                    statusn[lnum] = "Complete"
                elif len(donetasks[lnum]) >= len(taskgroup):
                    statusn[lnum] = "Almost Complete"
                elif len(donetasks[lnum]) > 0:
                    statusn[lnum] = "Inprogress"
                else:
                    statusn[lnum] = "Incomplete"
                print("Task Created!")

        case "3":
            if len(title) == 0:
                print("\nNo lists yet! create a list.")
            else:
                print("\nTodo's : ")
                for idx in range(0,(len(title))):
                    print(f"\n{idx}. List: {title[idx]}")
                    print(f"Description: {desc[idx]}")
                    print(f"Status : {statusn[idx]}")
                    print("Task's: ")
                    if tasks == []:
                        print("    No task's yet.")
                    elif len(tasks[idx]) == 0:
                        print("    No task's yet.")
                    else:
                        for tidx, task in enumerate(tasks[idx]):
                            print(f"    - {tidx+1}) {task}")
                    print("\nCompleted Task's: ")
                    if donetasks == []:
                        print("    No completed task's yet.")
                    elif len(donetasks[idx]) == 0:
                        print("    No completed task's yet.")
                    else:
                        for didx, dtask in enumerate(donetasks[idx]):
                            print(f"    - {didx+1}) {dtask}")

        case "4":
            if len(title) == 0:
                print("\nNo lists yet! create a list.")
            else:
                print("\nLists: ")
                for lcheck in range(0,(len(title))):
                    print(f"    - {title[lcheck]} ({lcheck})")
                lnum = int(input("\nList Number: "))
                print("\nTask's:")
                for tidx, task in enumerate(tasks[lnum]):
                            print(f"    - {tidx+1}) {task}")
                todo = int(input("\nTask number complete: "))
                checkTodo = todo-1
                taskgroup = tasks[lnum]
                donetasks[lnum].append(taskgroup[checkTodo])
                taskgroup.pop(checkTodo)
                if(len(donetasks[lnum]) != 0 and len(taskgroup) == 0):
                    statusn[lnum] = "Complete"
                elif len(donetasks[lnum]) >= len(taskgroup):
                    statusn[lnum] = "Almost Complete"
                elif len(donetasks[lnum]) > 0:
                    statusn[lnum] = "Inprogress"
                else:
                    statusn[lnum] = "Incomplete"
                print("\nDone!")
        
        case "5":
            if len(title) == 0:
                print("\nNo lists yet! create a list.")
            else:
                print("\nLists: ")
                for lcheck in range(0,(len(title))):
                    print(f"    - {title[lcheck]} ({lcheck})")
                lnum = int(input("\nList Number: "))
                editw = input("What to edit (Title/Desc): ")
                if editw == "Title":
                    title[lnum] = input("New title: ")
                elif editw == "Desc":
                    desc[lnum] = input("New Description: ")
                print("\nDone!")

        case "6":
            AddListElements("titles", title)
            AddListElements("descriptions", desc)
            AddListElements("statusn", statusn)
            AddTasks("tasks", tasks)
            AddTasks("dtasks", donetasks)
            print("\nSuccessfully Saved!")

        case "7":
            RemoveFile("titles")
            RemoveFile("descriptions")
            RemoveFile("tasks")
            RemoveFile("dtasks")
            RemoveFile("statusn")
            title = []
            desc = []
            tasks = []
            donetasks = []
            statusn = []
            print("\nDeleted all of the saves successfully!")

        case "8":
            filename = input("\nFile name: ")
            with open((filename + ".txt"), "w") as sfile:
                sfile.write("Todo's : \n\n")
                for idx in range(0,(len(title))):
                    sfile.write(f"\n{idx}. List: {title[idx]}\n")
                    sfile.write(f"Description: {desc[idx]}\n")
                    sfile.write(f"Status: {statusn[idx]}\n")
                    sfile.write("Task's: \n")
                    if tasks == []:
                        sfile.write("    No task's yet.")
                    elif len(tasks[idx]) == 0:
                        sfile.write("    No task's yet.")
                    else:
                        for tidx, task in enumerate(tasks[idx]):
                            sfile.write(f"    - {tidx+1}) {task}\n")
                    sfile.write("Completed Task's: \n")
                    if donetasks == []:
                        sfile.write("    No completed task's yet.")
                    elif len(donetasks[idx]) == 0:
                        sfile.write("    No completed task's yet.")
                    else:
                        for didx, dtask in enumerate(donetasks[idx]):
                            sfile.write(f"    - {didx+1}) {dtask}\n")
                    sfile.write(" \n")
            print("Done!")

        case "9":
            print("")
            PrintActions()

        case _:
            print("\nIncorrect Action")
