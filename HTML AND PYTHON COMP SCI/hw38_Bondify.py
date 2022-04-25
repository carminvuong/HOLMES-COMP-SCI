# Carmin Vuong
# hw38: slice and Bondify
# worked with no one
# advised by no one


def find( desideratum, within):
     # Return the lowest index in the string "within"
     # where the single character "desideratum" is found, or 
     # length of "within" if "desideratum" is not in "within"

    pos = 0
    while pos < len( within):
        if within[ pos] == desideratum: return pos
        pos += 1
    return len(within)

# tests on abcdef
#          012345
print( find( 'c', 'abcdef') == 2) # plain test
print( find( 'c', 'abccc') == 2)  # test "lowest index"
print( find( 'a', 'abcdef') == 0) # edge case
print( find( 'f', 'abcdef') == 5) # edge case
print( find( 'g', 'abcdef') == 6) # over-the-edge case

# ---------------------------------------------------------------------------------------------------------
def slice(input, startAt, stopBefore):

    subString = ""
    index = startAt

    while index < stopBefore:
        subString += input[index]
        index += 1
    
    return subString


# test cases for slice function    
print(slice("zzSlicezzz", 2, 7) == "Slice")
#            0123456789
print(slice("A", 0, 1) == "A")

print(slice("0123456789", 6, 9) == "678")

# ---------------------------------------------------------------------------------------------------------

def Bondify( firstyLasty):

    spaceIndex = find( " ", firstyLasty)
    
    lastName = slice(firstyLasty, spaceIndex+1, len(firstyLasty))
    bondStyle = lastName + ". " + firstyLasty + "."

    return bondStyle

# test cases
print(Bondify("Carmin Vuong") == "Vuong. Carmin Vuong.")
print(Bondify("William Shakespeare") == "Shakespeare. William Shakespeare.")
print(Bondify("James Bond") == "Bond. James Bond.")
print(Bondify("David Holmes") == "Holmes. David Holmes.")