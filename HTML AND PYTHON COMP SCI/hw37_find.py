# Carmin Vuong
# hw37: while too
# worked with no one
# advised by no one

def find(desideratum, within):
    # initialization
    index = 0

    # looping statment
    while index < len(within): # goes through every index of the string
        if within[index] == desideratum: 
            return index

        # update    
        index += 1

    return -1   # if the while loop ends (if the string doesn't contain the desideratum), -1 is returned


# test cases
print(find("a", "") == -1)
print(find("z", "asodoasjzioajsdz") == 8)
print(find("b", "bbbbbbbbbbbbbbbbb") == 0)
