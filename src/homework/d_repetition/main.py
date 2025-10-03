from repetition import get_factorial, sum_odd_numbers

def main():
    while True:
        print('\nHomework 4 Menu')
        print("1-Factorial")
        print("2-Sum of Odd Numbers")
        print("3-Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == '3':
            while True:
                try:
                    num = int(input("Enter a non-negative integer to calculate its factorial: "))
                    if num < 0:
                        print("Please enter a non-negative integer.")
                        continue
                    result = get_factorial(num)
                    print(f"The factorial of {num} is {result}.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid non-negative integer.")
        elif choice == '2':
            while True:
                try:
                    num = int(input("Enter a positive integer to sum odd numbers up to it: "))
                    if num <= 0:
                        print("Please enter a positive integer.")
                        continue
                    result = sum_odd_numbers(num)
                    print(f"The sum of odd numbers up to {num} is {result}.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid positive integer.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-3).")