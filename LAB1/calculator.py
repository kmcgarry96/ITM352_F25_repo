# calculator.py

# Simple calculator for basic math operations

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def main():
    print("Simple Calculator")
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            result = add(num1, num2)
            op = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            op = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            op = '*'
        elif choice == '4':
            result = divide(num1, num2)
            op = '/'
        else:
            print("Invalid operation choice.")
            continue

        print(f"{num1} {op} {num2} = {result}")

        again = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
