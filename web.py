import streamlit as st

import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To App")
st.subheader("This is my to do App")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a To Do:", placeholder="Add a To Do",
              on_change=add_todo, key="new_todo")
