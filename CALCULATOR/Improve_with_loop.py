while True:
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    operation = input("Choose operation (+, -, *, /): ")

    if operation == "+":
        print("Result:", num1 + num2)

    elif operation == "-":
        print("Result:", num1 - num2)

    elif operation == "*":
        print("Result:", num1 * num2)

    elif operation == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero")

    else:
        print("Invalid operation")

    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        break