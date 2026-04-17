def converter():
    while True:
        print("\nUnit Converter")
        print("1. KM to Meter")
        print("2. Celsius to Fahrenheit")
        print("3. Back")

        choice = input("Choose: ")

        if choice == "3":
            break

        try:
            value = float(input("Enter value: "))
        except:
            print("Invalid input ❌")
            continue

        if choice == "1":
            print("Meters:", value * 1000)
        elif choice == "2":
            print("Fahrenheit:", (value * 9/5) + 32)
        else:
            print("Invalid choice")