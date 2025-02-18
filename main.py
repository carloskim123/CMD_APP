import os
from pickle import NEWOBJ
import time
from db_manager import DatabaseManager
import random
import keyboard
from termcolor import colored

database = DatabaseManager()


def find_todo_by_id(todo_id):
    for todo in database.db:
        if todo['id'] == todo_id:
            return todo

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def run_menu():
    print("Welcome")
    print("Choose task: ")

    option =  int(input("Option: (1: New Todo, 2: View Todo, 3: Delete Todo, 4: Edit Todo, 5: Exit) ->: "))

    match option:
        case 1:
            new_todo()
        case 2:
            view_todos()
        case 3:
            delete_todo()
        case 4:
            edit_todo()
        case 5:
            exit()
        case _:
            return "Invalid command"


def new_todo():
    id = random.randint(999, 1999)
    title = input("Enter todo title: ")
    content = input("Enter todo content: ")

    database.add_entry(id, title, content)

    refresh(2)

def view_todos():
    todo_count = len(database.db)

    while keyboard.is_pressed('enter'):
        pass

    print("\n")
    if todo_count == 0:
        print(f"You have no todo's left today!!")
        refresh(2)
    else:
        print(f"You have {todo_count} todo's left today!!\n")
        # render todos
        print(colored("*\x1B[3mpress any key to return to main view\x1B[*", "green"))

        print("Todos: ")
        for todo in database.db:
            print(f"  - ({todo['id']}) {todo['title']}: {todo['content']}\n")

        while True:
            # Detect key press
            event = keyboard.read_event(suppress=True)

            if event.event_type == keyboard.KEY_DOWN and event.name != 'enter':
                refresh(0)

def delete_todo():
    todo_id = (int(input("Enter todo id: ")))

    if todo_id:
        database.remove_entry(todo_id)
        refresh(3)
    else:
        refresh(2)

def edit_todo():
    todo_id = int(input("Enter todo id: "))

    # todo = find_todo_by_id(todo_id)
    located_todo = {}

    for todo in database.db:
        if todo['id'] == todo_id:
            located_todo = todo

    print(type(located_todo)) # <class 'dict'>
    new_title = input(f'Edit todo title ({located_todo["title"]}): ')
    new_content = input(f'Edit todo title ({located_todo["content"]}): ')

    updated_todo = {"id": located_todo['id'], "title": new_title, "content": new_content}
    database.edit_entry(updated_todo)
    refresh(2)

def refresh(duration):
    time.sleep(duration)
    clear_screen()
    run_menu()

def run_app():
    clear_screen()
    run_menu()

run_app()
