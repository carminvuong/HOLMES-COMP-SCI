# Carmin Vuong
# hw36: while loops
# worked with Niki Chen
# advised by no one


def evenForward(string):
    # initialization
    index = 0
    newString = ""


    while index < len(string): # boolean

        # body
        newString = newString + string[index]

        # update
        index = index + 2
    return newString


# test cases
print(evenForward("0123456789")) # should return 02468
print(evenForward("O n l y T h e E v e n I n d e x e s")) # should return OnlyTheEvenIndexes
print(evenForward("AB")) # should return A

