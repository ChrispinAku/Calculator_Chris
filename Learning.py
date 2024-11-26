# Example of reading two integers
user_input = input("Enter two integers separated by space: ")
x, y = map(int, user_input.split())
print(f"You entered: {x} and {y}")