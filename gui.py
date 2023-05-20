import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To Do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="items",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button]],
                   font=["Helvetica", 20])

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["items"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["items"].update(values=todos)
        case "Edit":
            item = values["items"][0]
            new_todo = values["todo"] + "\n"
            todos = functions.get_todos()
            index = todos.index(item)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["items"].update(values=todos)
        case "items":
            window["todo"].update(value=values["items"][0])
        case sg.WIN_CLOSED:
            break

window.close()
