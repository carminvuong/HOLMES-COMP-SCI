# Carmin Vuong
# hw31: recover & finish if
# worked with Joseph Mei
# advised by no one


# ----------------- taxBracket function ------------------------

# Pre-condition: only accepts non-negative integers as inputs
def taxBracket(taxableIncome):
# Post-condition: returns the tax rate based on your input 

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
print(abs(taxBracket(6000) - 10/100) < 0.001)   # non edge case
print(abs(taxBracket(9876) - 12/100) < 0.001)   # edge case
print(abs(taxBracket(50888) - 22/100) < 0.001)   # non edge case
print(abs(taxBracket(163300) - 24/100) < 0.001)   # edge case
print(abs(taxBracket(200000) - 32/100) < 0.001)   # non edge case
print(abs(taxBracket(518401) - 37/100) < 0.001)   # edge case
