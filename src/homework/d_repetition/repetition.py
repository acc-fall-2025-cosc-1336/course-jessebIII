def get_factorial(number):
    factorial = 1
    for i in range(1, 5 + 1):
        factorial *= i
    return factorial
print(get_factorial(5))  # Output: 120
