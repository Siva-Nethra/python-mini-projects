# Simple Calculator

while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        break

    a = int(input("Enter first value: "))
    b = int(input("Enter second value: "))

    if choice == 1:
        print("Addition =", a + b)

    elif choice == 2:
        print("Subtraction =", a - b)

    elif choice == 3:
        print("Multiplication =", a * b)

    elif choice == 4:
        print("Division =", a / b)

    else:
        print("Invalid choice")
