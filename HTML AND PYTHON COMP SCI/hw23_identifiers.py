# Carmin Vuong
# hw23: identifiers
# worked with no one
# advised by no one

# well-named variables
fahrenheitToCelsiusScaleFactor = 5/9
subtruendForTemperature = 32

Phi = ((1+5**(1/2))/2)
conjugatePhi = ((1-5**(1/2))/2)
divisorForBinetsFormula = 5**(1/2)

# freezing point of water is a bit too special to be a good test.
# But it's easy!
print((32 - subtruendForTemperature) * fahrenheitToCelsiusScaleFactor)

# boiling point of water is classic

print((212 - subtruendForTemperature) * fahrenheitToCelsiusScaleFactor)
# room temperature is a value I know: 68F is 20C

print((68 - subtruendForTemperature) * fahrenheitToCelsiusScaleFactor)


#F_7
print(((Phi)**7 + (conjugatePhi)**7) / divisorForBinetsFormula)


#F_10
print(((Phi)**10 + (conjugatePhi)**10) / divisorForBinetsFormula)