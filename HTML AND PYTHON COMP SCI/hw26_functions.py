# Carmin Vuong
# hw26: functions
# worked with no one
# advised by no one



#----------------------------------------------------------
# Fahrenheit to Celsius conversion

# To scale the sizes of the degrees in the two scales, 
# compare the number of degrees in each scale between the
# boiling and freezing points of water.


#  Fahrenheit to Celsius Conversion
def FtoC(tempInF):
    waterFreezes_F = 32
    Degrees_F_per_C = (212 - waterFreezes_F ) / (100 - 0)
    return (tempInF - waterFreezes_F) / Degrees_F_per_C

# freezing point of water: 32 F -> 0 C
print( FtoC(32) )
 
# boiling point of water: 212 F -> 100 C
print( FtoC(212) )

# room temperature: 68F -> 20C
print( FtoC(68) )



# Celsius to Fahrenheit Conversion
def CtoF(tempInC):
    waterFreezes_F = 32
    Degrees_F_per_C = (212 - waterFreezes_F ) / (100 - 0)
    return (tempInC * Degrees_F_per_C) + waterFreezes_F

# freezing point of water: 0 C -> 32 F
print( CtoF(0) ) 

# boiling point of water: 100 C -> 212 F
print( CtoF(100) ) 

# room temperature: 20 C -> 68 F
print( CtoF(20) )