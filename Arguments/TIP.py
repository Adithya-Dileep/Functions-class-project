def tipwaiter(bill_amount, tip_percentage):
    tip_amount = bill_amount * (tip_percentage / 100)
    return round(tip_amount, 2)
print(tipwaiter(1000,10))