import numpy as np
import pandas as pd
import os

class ArithmeticOperations:
    """A class that performs basic arithmetic operations"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        """Returns the sum of two numbers"""
        return self.a + self.b

    def subtract(self):
        """Returns the difference of two numbers"""
        return self.a - self.b

    def multiply(self):
        """Returns the product of two numbers"""
        return self.a * self.b

    def divide(self):
        """Returns the division of two numbers"""
        if self.b == 0:
            return "Error! Division by zero."
        return self.a / self.b

def generate_random_data(rows=10, filename="output.csv"):
    """Generates a CSV file with random data"""
    data = {
        "A": np.random.randint(1, 100, rows),
        "B": np.random.randint(1, 100, rows)
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"CSV file '{filename}' has been created successfully!")

    print(os.getcwd())

# Test function
if __name__ == "__main__":
    generate_random_data()
    operation = ArithmeticOperations(10, 5)
    print("Addition:", operation.add())
    print("Subtraction:", operation.subtract())
    print("Multiplication:", operation.multiply())
    print("Division:", operation.divide())
    
