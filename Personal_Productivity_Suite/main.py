import notes
import calculator
import timer
import unit_converter
import file_organizer

notes.load_notes()

while True:
    print("\nMAIN MENU")
    print("1. Notes")
    print("2. Calculator")
    print("3. Timer")
    print("4. Unit Converter")
    print("5. File Organizer")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        notes.notes_menu()

    elif choice == "2":
        calculator.calculator()

    elif choice == "3":
        timer.timer()

    elif choice == "4":
        unit_converter.converter()

    elif choice == "5":
        file_organizer.organize()

    elif choice == "6":
        break

    else:
        print("Invalid choice")