# Carmin Vuong
# hw31: recover & finish if
# worked with Anthony Chen
# advised by no one


# ----------------- taxBracket function ------------------------
def taxBracket(taxableIncome):
    if taxableIncome <= 9875:
        return 10/100
    elif taxableIncome <= 40125:
        return 12/100
    elif taxableIncome <= 85525:
        return 22/100
    elif taxableIncome <= 163300:
        return 24/100
    elif taxableIncome <= 207350:
        return 32/100
    elif taxableIncome <= 518400:
        return 35/100
    else:
        return 37/100
    
    


# ---------------- test cases ------------------------
print(taxBracket(9000) == 10/100)   # non edge case
print(taxBracket(9876) == 12/100)   # edge case
print(taxBracket(50888) == 22/100)   # non edge case
print(taxBracket(163300) == 24/100)   # edge case
print(taxBracket(186000) == 32/100)   # non edge case
print(taxBracket(518401) == 37/100)   # edge case