import commands,json



if __name__ == "__main__":

    try:
        with open("Task Tracker/tasks.json","x") as file:
            file.write(json.dumps({"tasks":[],"aktId": 1},indent=4))
    except:
        pass


    print("""
    -----------------------
    exit - Exit Program
    help - List of Commands
    -----------------------
            """)
    userInput = [""]

    while (userInput[0]!="exit"):

        print("> ",end="")
        userInput = input().split()
        if (len(userInput)==0):
            print("Please type valid input!")
            continue

        if (userInput[0]=="help"): commands.help_commands(userInput)
        elif (userInput[0]=="add"): commands.add(userInput)
        elif (userInput[0]=="delete"): commands.delete(userInput)
        elif (userInput[0]=="update"): commands.update(userInput)
        elif (userInput[0]=="mark-in-progress"): commands.markInProgress(userInput)
        elif (userInput[0]=="mark-done"): commands.markDone(userInput)
        elif (userInput[0]=="list"): commands.listTasks(userInput)
        elif (userInput[0]!="exit"): print("Please type valid input!")

        print("\n")