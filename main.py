while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        todos.append(todo + "\n")
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif user_action.startswith("show"):
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.capitalize()
            print(f"{index+1}-{item}")
    elif user_action.startswith("edit"):
        try:
            todo_number = int(user_action[5:])
            todo_number = todo_number-1
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            print("Here is todos existing", todos)

            new_todo = input("Enter new ToDo item:")
            todos[todo_number] = new_todo + "\n"
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not Valid")
            continue
    elif user_action.startswith("complete"):
        try:
            todo_number = int(user_action[9:])
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            todo_number = todo_number-1
            todo_to_remove = todos[todo_number].strip("\n")
            todos.pop(todo_number)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

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
