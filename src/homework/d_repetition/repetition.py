def get_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def sum_odd_numbers(n):
    total = 0
    for i in range(1, n + 1, 2):
        total += i
    return total