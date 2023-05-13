def get_todos(filepath):
    """Read a text file and return the list of To-Do items"""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    """Write list of To-Do items into text file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
