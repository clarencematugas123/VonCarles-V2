def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a, b):
    return a ** b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
}


print("VonCarles Calculator")
print("Operations: +, -, *, /, ^")

while True:
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /, ^): ")
        num2 = float(input("Enter second number: "))

        if op not in operations:
            raise ValueError("Invalid operation.")

        result = operations[op](num1, num2)
        print(f"Result: {result}")
    except ValueError as error:
        print(f"Error: {error}")

    again = input("Would you like to do another calculation? (y/n): ").strip().lower()
    if again != "y":
        print("Goodbye!")
        break
