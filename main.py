from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos("todos.txt")
        todos.append(todo + "\n")
        write_todos('todos.txt', todos)
    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")
        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.capitalize()
            print(f"{index+1}-{item}")
    elif user_action.startswith("edit"):
        try:
            todo_number = int(user_action[5:])
            todo_number = todo_number-1
            todos = get_todos("todos.txt")
            print("Here is todos existing", todos)

            new_todo = input("Enter new ToDo item:")
            todos[todo_number] = new_todo + "\n"
            write_todos('todos.txt', todos)
        except IndexError:
            print("Your command is not Valid")
            continue
        except ValueError:
            print("Your command is not Valid")
            continue
    elif user_action.startswith("complete"):
        try:
            todo_number = int(user_action[9:])
            todos = get_todos("todos.txt")
            todo_number = todo_number-1
            todo_to_remove = todos[todo_number].strip("\n")
            todos.pop(todo_number)
            write_todos('todos.txt', todos)
            message = f"ToDo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no Item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")
print("Bye")
