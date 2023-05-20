FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of To-Do items"""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write list of To-Do items into text file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
