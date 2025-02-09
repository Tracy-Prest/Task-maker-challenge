# creating an empty to do list that we'll add, remove and view from 

# to_do_list = []
tasks = []
# # create task input
# enter_task = input("What are your task for the day? ")
# # create index of the list to write in
index = 0
# for i in to_do_list:
#     if to_do_list == None:
#        to_do_list.append("Go to the bank")

# print(to_do_list)

# add, remove and view functions
def add(task):
    tasks.append(task)
    print(f"Task '{task}' added")
        #   print("Task added")

def remove(task):
    if task in tasks:
          tasks.remove(task)
          print(f"Task '{task}' removed")
    else:
        print(f"Task '{task}' not found")
def view():
     if tasks:
         print("Your tasks: ")
         for i, task in enumerate (tasks, start=1): # for i in tasks:
            print(f"{i}. {task} ")
     else:
         print("You don\'t have any task")
    #     print(i, task) #just defined functions and what they should do
def mark_done(index):
    tasks[index] = tasks[index] + " Done"
    print(f"Task {tasks[index]} ")

def edit_task(index, edited):
        tasks[index] = edited      # view(task) 
        print(f"Task {index + 1} edited: {edited}")         # c_w = TextBlob(tasks)
    # if task != c_w:
    #     print("Edit your task")
    # else:
    #     print("Choose option to remove a task")
def reorder(index):
        print(f"Tasks reordered at index = {index}")

# def load_file():
#     fname = "change.txt"
    

def save_list_to_file():
    fname = "change.txt"
    with open(fname, 'a') as handle:  # convert list to string before writing
        handle.write("\n" .join(tasks) + "\n") # each task to a new line
    with open(fname, 'r') as handle:
        content = handle.read()
    print(content)



# option for main to do list and create a loop
while True:
    option = print("""Choose an option
     1. Add Task 
     2. Remove Task
     3. View Task
     4. Mark as done
     5. Edit Task
     6. Reorder Task
     7. Save Task in File
     8. Quit
     """)
    number = input("Enter option number: \n")
    if number == "1":
         task = input("Add a task: \n").strip().upper() 
         add(task)
         
    elif number == "2":
         view()
         tindex = int(input("Remove a task using its number: \n")) - 1
         if 0 <= tindex < len(tasks):
            remove(tasks[tindex])
         else:
             print("Invalid task number")
       
    elif number == "3":
        #  task = input("Display tasks")
         view()
    
    elif number == "4":
         view()
         tindex = int(input("Enter the task number to mark as done: \n")) - 1

         mark_done(tindex)

    elif number == "5":
        ask = input("do you want an edit? (yes or no) \n")
        if ask == "yes":
           view()
           try:
               tindex = int(input("Enter the task number you want to edit: \n")) - 1
               if 0 <= tindex < len(tasks):
                 edited = input("Enter the new task: \n").strip().upper()
                 edit_task(tindex, edited)
               else:
                print("Invalid task number")
           except IndexError:
               print("Invalid index")
        # else:
        #     # print("You don/'t need an edit")

    elif number == "6":
      view()
      if 0 <= index <len(tasks):
          task = tasks.pop(index)
          tasks.insert(0, task)
          reorder(index)
          print(f"Task '{task}' moved to the front of the list")
      else:
          print("Invalid index")      

    elif number == "7":
        view()
        save_file = input("Do you want to save list to file? (yes or no)\n").strip().lower()
        if save_file == "yes":
            
            save_list_to_file()

    elif number == "8":
         print("Thanks for using to do list")
         break
    else:
        print("Invalid number, choose a number from the option")

    # modify later