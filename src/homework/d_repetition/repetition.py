def get_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(get_factorial(5))  # 120
print(get_factorial(1))  # 1
print(get_factorial(0))  # 1

def sum_odd_numbers(n):
    total = 0
    for i in range(1, n + 1, 2):
        total += i
    return total
print(sum_odd_numbers(5))  # 9 (1 + 3 + 5)
print(sum_odd_numbers(1))  # 1