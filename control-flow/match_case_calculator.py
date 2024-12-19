!#/bin/bash
def calculate(num1, num2, operation):
    case '+':
        return num1 + num2
    case '-':
        return num1 - num2
    case '*':
        return num1 * num2
    case '/':
        if num2 == 0:
            return "Cannot divide by zero."
        else:
            return num1 / num2
    case -:
        return "Invalid operation."
def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")
    result = calculate(num1, num2, operation)
    print(f"The result is: {result}")
if __name__ == "__main__":
    main()
