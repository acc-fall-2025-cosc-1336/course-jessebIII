# named constant
TAX_RATE = 0.0675  # 6.75%

def get_sales_tax_amount(meal_amount: float) -> float:
    """Calculate the sales tax amount on a meal."""
    return meal_amount * TAX_RATE

def get_tip_amount(tip_amount: float) -> float:
    """Return the flat tip amount (not percentage)."""
    return tip_amount

def main():
    # get input from the user
    meal_amount = float(input("Enter the meal amount: "))
    tip_amount = float(input("Enter the tip amount (in dollars): "))

    # calculations using functions
    tax = get_sales_tax_amount(meal_amount)
    tip = get_tip_amount(tip_amount)
    total = meal_amount + tax + tip

    # display receipt
    print("\n-----receipt-----")
    print(f"meal amount: ${meal_amount:.2f}")
    print(f"sales tax:   ${tax:.2f}")
    print(f"tip amount:  ${tip:.2f}")
    print(f"total amount:${total:.2f}")

if __name__ == "__main__":
    main()
