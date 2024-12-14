class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == 'addition':
            return self.a + self.b
        elif self.operation == 'subtraction':
            return self.a - self.b
        elif self.operation == 'multiplication':
            return self.a * self.b
        elif self.operation == 'division':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Division by zero is not allowed."
        else:
            return "Invalid operation. Please choose from Addition, Subtraction, Multiplication, or Division."

# Example usage:
if __name__ == "__main__":
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))
    operation = input("Enter the type of operation (Addition, Subtraction, Multiplication, Division): ")

    calculator = Calculator(a, b, operation)
    result = calculator.calculate()
    print(f"The result of {operation} is: {result}")
