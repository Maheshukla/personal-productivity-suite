def calculator():
    while True:
        print("\nCalculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Back")

        choice = input("Choose: ")

        if choice == "5":
            break

        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except:
            print("Invalid input")
            continue

        if choice == "1":
            print("Result:", num1 + num2)
        elif choice == "2":
            print("Result:", num1 - num2)
        elif choice == "3":
            print("Result:", num1 * num2)
        elif choice == "4":
            print("Result:", num1 / num2)
        else:
            print("Invalid choice")