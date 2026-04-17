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
            print("Returning to Main Menu...")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except:
            print("Invalid input! Please enter numbers only.")
            continue

        if choice == "1":
            result = num1 + num2
            print("Result:", result)

            if num1 == num2:
                print("Both numbers are same!")

        elif choice == "2":
            result = num1 - num2
            print("Result:", result)

            if result == 0:
                print("Result is zero (perfect balance!)")

        elif choice == "3":
            result = num1 * num2
            print("Result:", result)

            if num1 == 0 or num2 == 0:
                print("Anything multiplied by 0 is 0")

        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                result = num1 / num2
                print("Result:", result)

                if result == 1:
                    print("Both numbers are equal!")
                elif result < 1:
                    print("Result is less than 1")

        else:
            print("Invalid choice")

        print("You can perform another calculation")