import json
import shutil

def backup_notes():
    try:
        shutil.copy("data/notes.json", "data/notes_backup.json")
        print("Backup created")
    except Exception as e:
        print("Backup failed")
        print(e)

notes = []

def save_notes():
    with open("data/notes.json", "w") as file:
        json.dump(notes, file)

def load_notes():
    global notes
    try:
        with open("data/notes.json", "r") as file:
            notes = json.load(file)
    except:
        notes = []

def add_note():
    note = input("Input note: ")
    notes.append(note)
    save_notes()
    backup_notes()  
    print("Note added")

def view_note():
    for i, note in enumerate(notes):
        print(i+1, note)

def delete_note():
    view_note()
    
    index = int(input("Kaunsa note delete karna hai: ")) - 1

    if 0 <= index < len(notes):
        notes.pop(index)
        save_notes()
        backup_notes()
        print("Note deleted")
    else:
        print("Invalid number")

def notes_menu():
    load_notes()

    while True:
        print("\n1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Back")

        choice = input("Choose: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            break
        else:
            print("Invalid choice")