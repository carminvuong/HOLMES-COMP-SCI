# Carmin Vuong
# hw37: while too
# worked with no one
# advised by no one

def alternatingReverse(string):
    # precondition: input is a string of text
    # postcondition: returns a string built from alternating indexes starting from the last character of the argument

    # initialization
    index = -1
    newString = ""

    # looping statement
    while index >= -len(string):

        # body
        newString += string[index]

        # update
        index -= 2
    return newString

    

# test cases
print(alternatingReverse("") == "")
print(alternatingReverse("0123456789") == "97531")
print(alternatingReverse("e s r e v e R g n i t a n r e t l a") == "alternatingReverse")