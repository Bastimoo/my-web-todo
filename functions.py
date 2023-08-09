def get_todos(filepath='todos.txt'):
    """Reads a text file and returns a list of to-do items"""
    with open(filepath, 'r') as file:
        todolist = file.readlines()
    return todolist

def get_completed(filepath='completelist.txt'):
    """Reads a text file and returns a list of completed items"""
    with open(filepath, 'r') as file:
        completelist = file.readlines()
    return completelist

def write_todos(todolist,filepath='todos.txt' ):
    """Writes the to-do items list to the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todolist)

def write_complete(completeitem,filepath='completelist.txt' ):
    """Writes the to-do items list to the text file"""
    completelist = get_completed()
    completelist.append(completeitem)
    with open(filepath, 'w') as file:
        file.writelines(completelist)

def show_list(todolist):
    """Displays the current to-do-list"""
    for index, item in enumerate(todolist):
        print(f"({index + 1}){item}")
    selection = input("Select an item.\n")
    return selection