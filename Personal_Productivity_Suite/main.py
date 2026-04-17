num1 = int(input("Pahla number likho: "))
num2 = int(input("Dusra number likho: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Devide ")

choice = input("Choose Option: ")

if choice == 1:
    print("Result:", num1 + num2)
elif choice ==2:
    print("Result:", num1 - num2)
elif choice == 3:
    print("Result:", num1 * num2)
elif choice == 4:
    print("Result:", num1 * num2)
else:
    print("Invalid Choice")