# named constant
TAX_RATE = 0.0675 #6.75%

def get_sales_tax_amount(meal_amount: float) -> float:
    """Calculate the sales tax amount on a meal."""
    return meal_amount * TAX_RATE

def get_tip_amount(meal_amount: float, tip_percentage: float) -> float:
    """Calculate the tip amount on a meal."""
    return meal_amount * tip_percentage # 

def main():
    #get input from the user
    meal_amount = float(input("Enter the meal amount: "))
    tip_percentage = float(input("Enter the tip percentage (as a decimal): "))

    #convert percentage to decimal
    tip_rate = tip_percentage / 100