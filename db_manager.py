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
    def edit_entry(self, index, new_title, new_content):
        if 0 <= index < len(self.db):  # Check if index is valid
            self.db[index]["title"] = new_title
            self.db[index]["content"] = new_content
            self.save_db()
            print(f"Edited entry {index}: {new_title}")
        else:
            print("Invalid index")

    # Method to remove an entry
    def remove_entry(self, index):
        if 0 <= index < len(self.db):  # Check if index is valid
            removed = self.db.pop(index)  # Remove the entry
            self.save_db()
            print(f"Removed: {removed['title']}")
        else:
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
