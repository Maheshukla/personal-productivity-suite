import json
notes = []

def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def load_notes():
    global notes
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except:
        notes = []

def add_note():
    note = input("Input note: ")
    notes.append(note)
    save_notes()
    print("Note added")

def view_note():
    for i, note in enumerate(notes):
        print(i+1, note)

def delete_note():
    save_notes()
    view_note()

    index = int(input("Kaunsa note delete karna hai: ")) - 1
    if 0<= index < len(notes):
        notes.pop(index)
        print("Note deleted")
    else:
        print("Invalid number")

load_notes()

while True:
    print("\n1. Add note: ")
    print("2. View note: ")
    print("3. Delete note: ")
    print("4. exit: ")

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
        
        


    
