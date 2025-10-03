def get_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(get_factorial(5))  # 120
print(get_factorial(1))  # 1
print(get_factorial(0))  # 1
