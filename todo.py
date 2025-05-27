import random,os,string,math

title = []
desc = []
tasks = []
donetasks = []
statusn = []

if os.path.exists("titles.txt"):
    with open("titles.txt", "r") as readd:
        title = readd.read().splitlines()

if os.path.exists("descriptions.txt"):
    with open("descriptions.txt", "r") as readd:
        desc = readd.read().splitlines()

if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as readd:
        content = readd.read().strip()
    if content:
        groups = content.split("\n\n")
        tasks = []
        for group in groups:
            if group:
                task_list = group.split("\n")
                tasks.append(task_list)
            else:
                tasks.append([])
    else:
        tasks.append([])

if os.path.exists("dtasks.txt"):
    with open("dtasks.txt", "r") as readd:
        content = readd.read().strip()
    if content:
        groups = content.split("\n\n")
        donetasks = []
        for group in groups:
            if group:
                dtask_list = group.split("\n")
                donetasks.append(dtask_list)
            else:
                donetasks.append([])
    else:
        donetasks.append([])

if os.path.exists("statusn.txt"):
    with open("statusn.txt", "r") as readd:
        statusn = readd.read().splitlines()

os.system("cls")

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

while True:
    action = input("\nAction: ")
    
    if action == "1":
        title.append(input("\nTitle: "))
        desc.append(input("Description: "))
        tasks.append([])
        donetasks.append([])
        statusn.append("Incomplete")
        print("List Created!")

    elif action == "2":
        if len(title) == 0:
            print("\nNo lists yet! create a list.")
        else:
            print("\nLists : ")
            for lcheck in range(0,(len(title))):
                print(f"    - {title[lcheck]} ({lcheck})")
            lnum = int(input("\nList Number: "))
            todo = input("Task to add: ")
            tasks[lnum].append(todo)
            wah = tasks[lnum]
            if(len(donetasks[lnum]) != 0 and len(wah) == 0):
                statusn[lnum] = "Complete"
            elif len(donetasks[lnum]) >= len(wah):
                statusn[lnum] = "Almost Complete"
            else:
                statusn[lnum] = "Incomplete"
            print("Task Created!")

    elif action == "3":
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
                    for dtidx, dtask in enumerate(donetasks[idx]):
                        print(f"    - {dtidx+1}) {dtask}")

    elif action == "4":
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
            lol = todo-1
            wah = tasks[lnum]
            donetasks[lnum].append(wah[lol])
            wah.pop(lol)
            if(len(donetasks[lnum]) != 0 and len(wah) == 0):
                statusn[lnum] = "Complete"
            elif len(donetasks[lnum]) >= len(wah):
                statusn[lnum] = "Almost Complete"
            else:
                statusn[lnum] = "Incomplete"
            print("\nDone!")
    
    elif action == "5":
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

    elif action == "6":
        with open("titles.txt", "w") as titless:
            titless.write("\n".join(title) + "\n")

        with open("descriptions.txt", "w") as descs:
            descs.write("\n".join(desc) + "\n")

        with open("tasks.txt", "w") as taskss:
            for task_list in tasks:
                if task_list:
                    taskss.write("\n".join(task_list))
                    taskss.write("\n\n")
                else:
                    taskss.write("\n\n")

        with open("dtasks.txt", "w") as dtaskss:
            for dtask_list in donetasks:
                if dtask_list:
                    dtaskss.write("\n".join(dtask_list))
                    dtaskss.write("\n\n")
                else:
                    dtaskss.write("\n\n")


        with open("statusn.txt", "w") as statusns:
            statusns.write("\n".join(statusn) + "\n")

        print("\nSuccessfully Saved!")

    elif action == "7":
        delwhar = "all"
        if delwhar == "all":
            if os.path.exists("titles.txt"):
                os.remove("titles.txt")
            if os.path.exists("descriptions.txt"):
                os.remove("descriptions.txt")
            if os.path.exists("tasks.txt"):
                os.remove("tasks.txt")
            if os.path.exists("dtasks.txt"):
                os.remove("dtasks.txt")
            if os.path.exists("statusn.txt"):
                os.remove("statusn.txt")
            title = []
            desc = []
            tasks = []
            donetasks = []
            statusn = []
            print("\nDeleted all of the saves successfully!")

    elif action == "8":
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
                    for dtidx, dtask in enumerate(donetasks[idx]):
                        sfile.write(f"    - {dtidx+1}) {dtask}\n")
                sfile.write(" \n")
        print("Done!")

    elif action == "9":
        print("\nActions : ")
        print("    1) Create list")
        print("    2) Add Todo")
        print("    3) Check Todo's")
        print("    4) Complete Task")
        print("    5) Configure List")
        print("    6) Save Todo's")
        print("    7) Delete Saves")
        print("    8) Export to Txt")
        print("    9) Actions")

    else:
        print("\nIncorrect Action")