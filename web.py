import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = "\n" + st.session_state["new_todo"]
    todos.append(todo)
    functions.write_todo(todos)


st.title("My ToDo Web App")

for index, todo in enumerate(todos):
    checked = st.checkbox(todo, key=todo)
    if checked:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter ToDo:", placeholder="Enter todos ....", on_change=add_todo, key="new_todo")


