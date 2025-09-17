# A simple program to multiply two numbers

def multiply_numbers(a, b):
    """Return the product of two numbers."""
    return a * b

def main():
    # First multiplication: 7 x 7
    num1 = 7
    num2 = 7
    result1 = multiply_numbers(num1, num2)
    print(f"The product of {num1} and {num2} is {result1}")



# Run the program
if __name__ == "__main__":
    main()