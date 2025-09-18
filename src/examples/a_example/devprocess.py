# Echo function returns the input value
def echo_value(x):
    return x

# Add two numbers and return the result
def add_numbers(a, b):
    return a + b
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

    # Second multiplication: 5 x 5
    num3 = 5
    num4 = 5
    result2 = multiply_numbers(num3, num4)
    print(f"The product of {num3} and {num4} is {result2}")


# Run the program
if __name__ == "__main__":
    main()