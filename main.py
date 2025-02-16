import os
import time
from db_manager import DatabaseManager
import random
import keyboard
from termcolor import colored

database = DatabaseManager()



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
        # case 4:
            # edit_todo()
        case 5:
            exit()
        case _:
            return "Invalid command"


def new_todo():
    id = random.randint(999, 1999)
    title = input("Enter todo title: ")
    content = input("Enter todo content: ")

    database.add_entry(id, title, content)

    refresh()

def view_todos():

    todo_count = len(database.db)

    if todo_count == 0:
        print(f"You have no todo's left today!!")
        refresh()
    else:
        print(f"You have {todo_count} todo's left today!!\n")
        # render todos
        for todo in database.db:
            print(colored("*\x1B[3mpress any key to return to main view\x1B[*", "green"))
            print("Todos: ")
            print(f"  - ({todo['id']}) {todo['title']}: {todo['content']}\n")

            # Detect keypress to

def delete_todo():
    return

def refresh():
    time.sleep(2)
    clear_screen()
    run_menu()

def run_app():
    clear_screen()
    run_menu()

run_app()
