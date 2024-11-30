import streamlit as st
from streamlit import session_state

import todolist
import fileops
import task

def web_add_todo():
    todo= st.session_state["new_todo"]
    deadline=st.session_state["new_deadline"]
    print(todo)
    print(deadline)
    app_todos.gui_add_task(todo,str(deadline))

#intialised todo and load up for first time
app_todos=todolist.TaskList()
app_todos.gui_retrieve_task()


#print title and intro
st.title("Ben's todo app")
st.subheader("This is Ben's implementation of todo")
st.write("This app is to boost your productivity")

#print todos in a checkbox format (
for index,todo in enumerate(app_todos):
    checkbox=st.checkbox(f"Task: {todo.return_todo()}  \nDeadline: {todo.return_deadline()}",key=index)
    if checkbox:
        app_todos.web_complete_task(index)  #Uses a function
        st.rerun()    #Rerun the page after deleting

#items for creating add to do
st.text_input("Enter a todo",key="new_todo")
st.date_input("Enter a deadline",key="new_deadline")
st.button("Add",on_click=web_add_todo )




