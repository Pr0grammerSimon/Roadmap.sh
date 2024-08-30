import json,time,dataclasses

def help_commands(userInput):
  if (len(userInput) > 1): 
    print("Help command don't take parameters!")
    return
  
  print("""
      !This is Help File!
      -----------------------------
      delete idOfTask - delete the task
      add "nameOfTask" - add the task 
      update idOfTask "nameOfNewTask" - update description of task
        
      mark-done idOfTask - mark task that is done
      mark-in-progress - mark task that is in progress
        
      list - list all Task
      list typeOfStatus - list all of tasks with that status 
        
      exit - exit Program
        """)
    



def add(userInput:list):
  #Checking if input is correct

  if (len(userInput)<2): 
    print("Add command take 1 parameter, string - name of task! Type help for more information")
    return

  elif (userInput[1][0]!='"' or userInput[-1][-1] != '"'): 
    print('Type of name must be an string and looks like - add "name of task" ')
    return
  
  elif (len(userInput)==2 and len(userInput[1])<3): 
    print("Name must not have be empty!")
    return
  
  #Input Correct - Program

  name =[]
  for idx in range(1,len(userInput)):
    name.append(userInput[idx])
  name = " ".join(name)

  if (len(name)>20):
    print("Name of Task must be equal or less than 20")
    return
  


  with open("Task Tracker/tasks.json",'r') as tasks:
    data = json.load(tasks)


  data['tasks'].append(
    {
      'id' : data['aktId'],
      'description' : name[1:-1],
      'status' : 'todo',
      'createdAt' : time.time(),
      'updatedAt' : time.time()
    }
  )

  data['aktId']+=1

  with open("Task Tracker/tasks.json",'w') as tasks:
    tasks.write(json.dumps(data,indent=4))
  
  print(f"Task added successfully (ID: {data['aktId']-1})")





def delete(userInput):
  #Cheking if input is correct 
  if (len(userInput)!=2): 
    print("Delete command take 1 parameter, number - id of task! Type help for more information")
    return
  
  #Checking if input is a number
  try:
    id = int(userInput[1])
  except:
    print('Type of id must be an number and looks like - delete id ')
    return
  
  #Input correct - Program
  

  with open("Task Tracker/tasks.json","r") as file:
    data = json.load(file)

  with open("Task Tracker/tasks.json","w") as file:
    new_tasks = list(filter(lambda item: item["id"]!=id ,data['tasks']))
    data["tasks"] = new_tasks
    file.write(json.dumps(data,indent=4))
    




def update(userInput):
  #Checking if input is correct

  if (len(userInput)<3): 
    print("Update command take 2 parameters, number - id and string - name of task! Type help for more information")
    return

  elif (userInput[2][0]!='"' or userInput[-1][-1] != '"'): 
    print('Type of name must be an string and looks like - add "name of task" ')
    return
  
  elif (len(userInput)==3 and len(userInput[2])<3): 
    print("Name must not have be empty!")
    return
  
  try:
    id = int(userInput[1])
  except:
    print("Invalid ID!")
    return

  #Input Correct - Program

  name =[]
  for idx in range(2,len(userInput)):
    name.append(userInput[idx])
  name = " ".join(name)

  if (len(name)>20):
    print("Name of Task must be equal or less than 20")
    return


  with open("Task Tracker/tasks.json",'r') as tasks:
    data = json.load(tasks)



  for item in data["tasks"]:
    if item["id"]==id:
      item["description"] = name[1:-1]
      item["updatedAt"] = time.time()



  with open("Task Tracker/tasks.json",'w') as tasks:
    tasks.write(json.dumps(data,indent=4))
  
  print(f"Task updated successfully!")





def listTasks(userInput):
  #Checking if input is correct
  if (len(userInput)>2): 
    print("List command take 0 or 1 parameter, string - what type to list in output! Type help for more information")
    return

  if (len(userInput)==1):
    with open("Task Tracker/tasks.json","r") as file:
      data = json.load(file)
      for item in data["tasks"]:
        print(f"Id: {item["id"]:<5} || Description: {item["description"]:<20} || Status: {item["status"]:<11} || Created At : {time.ctime(item["createdAt"])} || Updated At : {time.ctime(item["updatedAt"])}")
  else:
    with open("Task Tracker/tasks.json","r") as file:
      data = json.load(file)
      data = list(filter(lambda item: item["status"]==userInput[1], data['tasks']))
      for item in data:
        print(f"Id: {item["id"]:<5} || Description: {item["description"]:<20} || Status: {item["status"]:<11} || Created At : {time.ctime(item["createdAt"])} || Updated At : {time.ctime(item["updatedAt"])}")




def mark(newStatus,id):
  with open("Task Tracker/tasks.json",'r') as tasks:
    data = json.load(tasks)

  for item in data["tasks"]:
    if item["id"]==id:
      item["status"] = newStatus
      item["updatedAt"] = time.time()


  with open("Task Tracker/tasks.json",'w') as tasks:
    tasks.write(json.dumps(data,indent=4))

  print(f"Task updated successfully!")



def markInProgress(userInput):
  #Checking if input is correct
  if (len(userInput) != 2): print("Invalid input! mark-in-progress takes one argument!")
  try:
    id = int(userInput[1])
  except:
    print("Invalid ID!")
    return
  
  mark("in-progress",id)



def markDone(userInput):
  #Checking if input is correct
  if (len(userInput) != 2): print("Invalid input! mark-done takes one argument!")
  try:
    id = int(userInput[1])
  except:
    print("Invalid ID!")
    return
  
  mark("done",id)

  
