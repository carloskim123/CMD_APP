import pickle

DB_FILE = "database.pkl"  # The file where we store the data

class DatabaseManager:
    def __init__(self):
        self.db = self.load_db()  # Load once when the class is initialized

    # Method to load the database
    def load_db(self):
        try:
            with open(DB_FILE, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []  # Return empty list if file doesn't exist

    # Method to save the database
    def save_db(self):
        with open(DB_FILE, "wb") as f:
            pickle.dump(self.db, f)

    # Method to add an entry
    def add_entry(self, id, title, content):
        self.db.append({"id": id, "title": title, "content": content})
        self.save_db()  # Automatically save after adding
        print("Added:", title)

    # Method to edit an entry
    def edit_entry(self, edited_todo):
         # Check if index is valid
         for todo in self.db:
            if todo['id'] == edited_todo['id']:
                todo['title'] = edited_todo['title']
                todo["content"] = edited_todo['content']
                self.save_db()
                print(f"Edited entry {todo['id']}: {todo['title']}")

    # Method to remove an entry
    def remove_entry(self, todo_id):
        found = False # track if the todo is found

        for todo in self.db:  # Iterate the db
            if todo["id"] == todo_id:
                # Remove the entry
                print(f"Removed: {todo['title']}")

                self.db.remove(todo)
                self.save_db()
                found = True
                continue

        if not found:
            print("Invalid index")

    # Method to display all entries
    def show_entries(self):
        if not self.db:
            print("Database is empty.")
        else:
            for i, entry in enumerate(self.db):
                print(f"{i}. {entry['title']} - {entry['content']}")

# Create a single instance of DatabaseManager
database = DatabaseManager()
