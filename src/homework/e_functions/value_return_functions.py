FICA_RATE = 0.0765
FEDERAL_TAX_RATE = 0.08

def get_gross_pay(hours, rate):
    if hours > 40:
        regular_hours = 40
        overtime_hours = hours - 40
        gross_pay = (regular_hours * rate) + (overtime_hours * rate * 1.5)
    else:
        gross_pay = hours * rate
    return gross_pay

def get_fica_tax(gross_pay):
    return gross_pay * FICA_RATE

def get_federal_tax(gross_pay):
    return gross_pay * FEDERAL_TAX_RATE