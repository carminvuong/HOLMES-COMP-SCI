# Carmin Vuong
# hw30: autotip
# worked with no one
# advised by no one

def tipRate( partySize):
    'Return the tip rate to be added to the bill.'
    
    if partySize >= 8:
        return 0.18
    else:
        return 0.0
    


print( 'tests of tipRate')
print( tipRate( 10))
print( '...should be 0.18' )

print( tipRate( 8))
print( '...should be 0.18' )

print( tipRate( 2))
print( '...should be 0.0' )

print()


def autotip( foodCost, partySize):
    'Return the bill amount including tip.'


    return foodCost * (1 + tipRate( partySize))

print( 'tests of autotip()')
print( autotip( 100.00, 12))
print( '...should be 118' )

print( autotip( 40.00, 4))
print( '...should be 40' )

print( autotip( 17.50, 2))
print( '...should be 17.50' )

print()

# --------------------------------------------------
def tipRate( partySize):
    'Return the tip rate to be added to the bill.'
    
    if partySize >= 8:
        return 0.18
    else:
        if partySize >= 4:
            return 0.15
        else:
            return 0.0
# --------------------------------------------------



print( 'tests of autotip ***WITH 3-WAY tipRate***')
print( autotip( 100.00, 12))
print( '...should be 118' )

print( autotip( 40.00, 4))
print( '...should be 46, unlike previous value of 40' )

print( autotip( 17.50, 2))
print( '...should be 17.50' )

print()



