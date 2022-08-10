
to_do_list = []
task_list = [
    "Add a Task",            # 01
    "Remove A Task",         # 02
    "Show the to_do_list!",  # 03
    "Mark an Item Completed",  # 04
    "Quit The Prgrm"]        # 05


def countTasks():
    return len(task_list)


def printTasks():
    for id, i in enumerate(task_list):
        print("{:02d} {}!".format(id+1, i))


def countToDoList():
    return len(to_do_list)


def printToDoList():
    if not len(to_do_list):
        print("  §§ Oops, There is Nothing To do! yyeey §§")
        return 0
    print('\n', '#'*40)
    print("# N² - State - What To Do!!", end="")
    print('\n---------------------------')
    for id, i in enumerate(to_do_list):
        print("# {:02d} - {} - {}".format(id+1, i["state"], i["titem"]))
    print('#'*40)
    input('>> any key to quit! ')
    return 1


def addToDoListItem(perform):
    to_do_list.append({"state": "WAit",
                       "titem": perform})
    print("§§ DONE §§")


def removeToDoListItem(itemIndex):
    to_do_list.pop(itemIndex-1)
    return


def markItemCompleted(itemIndex):
    if to_do_list[itemIndex-1]["state"] == "Done":
        print("  §§ xD alredy completed!! §§ ")
    else:
        to_do_list[itemIndex-1]["state"] = "Done"
        print("  §§ yeey, another task completed §§")
    for item in to_do_list:
        if item["state"] != "Done":
            break
    else:
        print("  BTW  §§ NOICE DUD! §§\n       §§ALL TASKs CompLeteD §§")


def performTask(task_choice):
    ####################################
    # quit, Tbh hadi zyada ghla6t :")
    if task_choice == countTasks():
        pass
    ####################################
    # Add a Task
    elif task_choice == 1:
        perform = input(">> What task to Add!! ").strip()
        addToDoListItem(perform)
    ####################################
    # remove a task
    elif task_choice == 2:
        if printToDoList():
            while(True):  # bech nedi numm te3 task kayen fel list
                try:
                    perform = int(input(">> What task to Remove!!").strip())
                except ValueError as identifier:
                    print(f"  §§ Oopss {identifier} §§")
                else:
                    if 0 < perform < countToDoList()+1:
                        break
                    else:
                        print("§§ Oopss, Give a number between {} and {} §§".format(
                            1, countToDoList()))

            removeToDoListItem(perform)
    ####################################
    # "Show the to_do_list!",  # 03
    elif task_choice == 3:
        printToDoList()
    ####################################
    # "Mark a Item Completed",  # 04
    elif task_choice == 4:
        if printToDoList():
            while(True):  # bech nedi numm te3 task kayen fel list
                try:
                    perform = int(
                        input(">> What task to Mark Completed!!").strip())
                except ValueError as identifier:
                    print("  §§ Oopss §§")
                else:
                    if 0 < perform < countToDoList()+1:
                        break
                    else:
                        print("  §§ Oopss, Give a number from {} to {} §§".format(
                            1, countToDoList()))

            markItemCompleted(perform)

    return None
