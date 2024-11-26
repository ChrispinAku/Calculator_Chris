def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Welcome to the Calculator!")
    print("You can perform calculations by typing an expression.")
    print("Type 'exit' to end the program.")

    while True:
        # Get user input for numbers and operation
        user_input = input("Enter two integers separated by space and the operation (e.g., 3 4 +): ")
        
        if user_input.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        
        try:
            # Split the input into numbers and operation
            parts = user_input.split()
            num1 = int(parts[0])
            num2 = int(parts[1])
            operation = parts[2]
        except (ValueError, IndexError):
            print("Invalid input! Please enter two integers followed by an operation (+, -, *, /).")
            continue

        # Perform the operation based on user input
        if operation == '+':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif operation == '-':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif operation == '*':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif operation == '/':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid operation! Please use +, -, *, or /.")

if __name__ == "__main__":
    calculator()