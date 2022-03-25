# Carmin Vuong
# hw26: functions
# worked with no one
# advised by no one



#----------------------------------------------------------
# Fahrenheit to Celsius conversion

# To scale the sizes of the degrees in the two scales, 
# compare the number of degrees in each scale between the
# boiling and freezing points of water.

def FtoC():
    return 1
waterFreezes_F = 32
Degrees_F_per_C = (212 - waterFreezes_F ) / (100 - 0)

# freezing point of water: 32 F -> 0 C
print( (32 - waterFreezes_F) / Degrees_F_per_C )

# boiling point of water: 212 F -> 100 C
print( (212 - waterFreezes_F) / Degrees_F_per_C )

# room temperature: 68F -> 20C
print( (68 - waterFreezes_F) / Degrees_F_per_C )


#----------------------------------------------------------
# Calculate specific Fibonnaci number using Binet's formula
sqrt_five = 5 ** (1/2)
phi = (1+sqrt_five)/2
phi_conjugate = (1-sqrt_five)/2   # aka "psi"

#7th Fibonacci number: expecting 13
print( (phi**7 - phi_conjugate**7) / sqrt_five )

#10th Fibonacci number: expecting 55
print( (phi**10 - phi_conjugate**10) / sqrt_five )