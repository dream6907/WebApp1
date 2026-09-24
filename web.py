import streamlit as st
import functions

# correct way to run streamlit on the terminal is:
# python -m streamlit run web.py
# (because when run as: streamlit run web.py it requests admin access

# (.venv) PS C:\Users\daniel.momot\PycharmProjects\todo_app>
# python -m streamlit run web.py
# 2026-09-23 13:58:17.334 Uvicorn server started on :::8501
#
#   You can now view your Streamlit app in your browser.
#
#   Local URL: http://localhost:8501
#   Network URL: http://192.168.13.52:8501
#
#   Help agents write better Streamlit apps?
#   Install the official Streamlit skills by running streamlit
#   skills in your terminal.

#for Heroku deployment make sure you have the setup.sh and Procfile files
# and that you generated requirements.txt file with:
# pip freeze > requirements.tx


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
