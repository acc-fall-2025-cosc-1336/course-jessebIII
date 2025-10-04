from decisions import get_letter_grade  # adjust import if needed

def main():
    print("MAIN MENU\n")
    print("1-Letter grade using if")
    print("2-Letter grade using switch")
    print("3-Exit")
    choice = input("Enter your choice (1-3): ")

    if choice in ['1', '2']:
        try:
            score = float(input("Enter a numeric score (0-100): "))
            if 0 <= score <= 100:
                print(f"Letter grade: {get_letter_grade(score)}")
            else:
                print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    elif choice == '3':
        print("Exiting program.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()