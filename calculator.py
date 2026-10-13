def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "Error: Division by zero" #zero division error
    else:
        return a/b

def show_menu():
    print("\nSimple Calculator")
    print("Operations: add, subtract, multiply, divide")
    print("Type 'exit' to quit.")


def get_number(prompt):
    while True:
        text = input(prompt).strip()
        if text.lower() == "exit":
            return "exit"
        try:
            return float(text)
        except ValueError:
            print("Please enter a valid number, or type 'exit'.")

def main():
    while True:
        show_menu()
        operation = input("Enter operation: ").strip().lower()
        if operation == "exit":
            print("Thank you for using the calculator. Goodbye!")
            break
        if operation not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid operation. Please try again.")
            continue
        num1 = get_number("Enter first number: ")
        if num1 == "exit":
            print("Thank you for using the calculator. Goodbye!")
            break
        num2 = get_number("Enter second number: ")
        if num2 == "exit":
            print("Thank you for using the calculator. Goodbye!")
            break
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = sub(num1, num2)
        elif operation == "multiply":
            result = mul(num1, num2)
        elif operation == "divide":
            result = div(num1, num2)
        else:
            print("Invalid operation. Please try again.")
            continue
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
    