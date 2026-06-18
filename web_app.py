# python -m streamlit run web_app.py
import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("Hello, Streamlit!")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    # Use index to guarantee uniqueness
    checkbox = st.checkbox(todo, key=f"{todo}_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{todo}_{index}"]
        st.rerun()

st.text_input(
    label="Enter a todo",
    placeholder="Add new todo..",
    on_change=add_todo,
    key="new_todo"
)