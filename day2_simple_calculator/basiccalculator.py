def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print(" +  for Addition")
    print(" -  for Subtraction")
    print(" *  for Multiplication")
    print(" /  for Division")

    # Get user input
    num1 = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Perform calculation
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operation.")
        return

    print(f"Result: {num1} {op} {num2} = {result}")

# Run the calculator
calculator()
