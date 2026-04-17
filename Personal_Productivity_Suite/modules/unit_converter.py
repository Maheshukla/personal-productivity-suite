def converter():
    while True:
        print("\nUnit Converter")
        print("1. KM to Meter")
        print("2. Celsius to Fahrenheit")
        print("3. Back")

        choice = input("Choose: ")

        if choice == "3":
            print("Returning to Main Menu...")
            break

        try:
            value = float(input("Enter value: "))
        except:
            print("Invalid input! Please enter a number.")
            continue

        if choice == "1":
            result = value * 1000
            print("Meters:", result)

            if value == 0:
                print("0 KM means no distance!")
            elif value < 0:
                print("Negative distance? That's unusual!")
            elif value >= 100:
                print("That's a long distance!")

        elif choice == "2":
            result = (value * 9/5) + 32
            print("Fahrenheit:", result)

            if value == -40:
                print("Wow! -40°C = -40°F (Rare temperature point!)")
            elif value == 0:
                print("Freezing point of water")
            elif value == 100:
                print("Boiling point of water")
            elif value < 0:
                print("Very cold temperature!")

        else:
            print("Invalid choice")

        print("Try another conversion")