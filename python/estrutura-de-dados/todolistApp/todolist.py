import os, time
from logo import logo
# só pra não bagunçar ainda mais

name = "name"     # making it 
status = "status" # easier to read

taskList = [{name: "take a shower", 
             status: "done"},

            {name: "study math for ml", 
             status: "not done"},

            {name: "finish OOP assignment",
             status: "not done"},

            {name: "have lunch",
             status: "done"},

            {name: "read one piece ch.1132",
             status: "not done"},

            {name: "drink water",
             status: "not done"}]

def addTask(task):
    if searchTask(task):
        print(f'Error: task already exists.')
        return None
    global name, status
    taskList.append({name: task, status: "not done"})
    print("Task added.")

def searchTask(querry):
    for task in taskList:
        if querry.lower() in task["name"].lower():
            result = taskList.index(task)
            print(f"Task found at index [{result}].")
            return result
    return None

def doTask(task):
    if searchTask(task) == None:
        print("Error: task not found.")
        return
    global status
    task = taskList[searchTask(task)]
    task.update({status: "done"})
    print(f"Task {task[name]} status changed with sucess (done).")

def removeTask(task):
    taskIndex = searchTask(task) # this is a workaround for the code below 
    
    if taskIndex == None:
        print("Error: task not found.")
        return 
    
    if input('Are you sure you want to delete this task permanently? Type "confirm" to confirm: ').lower() != 'confirm':
            return
    task = taskList[taskIndex] 
    print(task)
    taskList.pop(taskIndex) 
    # for some reason, I couldn't just use "del task", so I had to
    # change the the search function to return a index instead of the
    # full task.
    print("Task deleted.")
    
def clearList(option):
    removed = 0
    if option == "1": # remove only already done tasks
        global status
        for task in taskList:
            if task[status] == "done":
                taskList.remove(task)
                removed += 1
        print(f"{removed} tasks removed.")
    
    elif option == "2": #remove all tasks
        if input('Are you sure you want delete all the tasks permanently? Type "confirm" to confirm: ').lower() != 'confirm':
            return
        removed = len(taskList)
        taskList.clear()
        print("List (removed) cleared with sucess.")
    else:
        print("Error: invalid argument.")

def showTaskList():
    global name, status
    counter = 1
    print("Tasks:")
    for task in taskList:
        print(f"{counter}) {task[name]} ({task[status]})")
        counter += 1

def showNotDone():
    global name, status
    counter = 1
    print("Tasks that haven't been done yet:")
    for task in taskList:
        if task[status] == "not done":
            print(f"{counter}) {task[name]}")
            counter += 1

def main():
    while True:
        os.system('clear')
        print(logo)
        match input('1. Add a task.\n2. Change task status.\n3. Remove a task.\n4. Show all tasks.\n5. Show only tasks that are not done.\n6. Search for a task.\n7. Clear task list.\n\nOption: '):
            case "1":
                addTask(input("Task: "))
            case "2":
                doTask(input("Task: "))
            case "3":
                removeTask(input("Task: "))
            case "4":
                showTaskList()
                input("Press [Enter] to continue.")
            case "5":
                showNotDone()
                input("Press [Enter] to continue.")
            case "6":
                taskIndex = searchTask(input("Task name: "))
                print("No tasks found.") if taskIndex == None else print(f"Task: {taskList[taskIndex]["name"]}\t Status: {taskList[taskIndex]["status"]}")
                input("Press [Enter] to continue.")
            case "7":
                clearList(input("\n1. Clear all done tasks.\n2. Clear all tasks.\n\nOption: "))
            case _ :
                if (input('Invalid option. Type "no" if you do not want to leave: ').lower()) != "no":
                    break
                
        time.sleep(1)
        os.system('clear')
    
if __name__ == "__main__":
    main()