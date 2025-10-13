def get_gross_pay(hours, rate):
    if hours > 40:
        regular hours = 40
        overtime_hours = hours - 40
        gross_pay = (regular_hours * rate) + (overtime_hours * rate * 1.5)
    else:
        gross_pay = hours * rate
    return gross_pay

def get_fica_tax(gross_pay):
    fica_tax = gross_pay * 0.0765
    return gross pay - fica_tax

def get_federal_tax(gross_pay):
    return gross_pay * federal_tax_rate