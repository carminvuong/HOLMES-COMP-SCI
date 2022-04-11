# Carmin Vuong
# hw35: string indexes
# worked with Anthony Chen
# advised by no one


def evenForward24(string):
    # precondition: input string with exactly 24 characters
    # postcondition: returns a string containing the even numbered characters of the argument

    newString = (string[0] + string[2] + string[4] + string[6]
         + string[8] + string[10]+ string[12] + string[14] + string[16] + string[18] + string[20] + string[22])
    return newString

def alternatingReverse23(string):
    # precondition: input string with exactly 23 characters
    # postcondition: returns a string with alternating characters starting from the last character of the argument
    newString = (string[-1] + string[-3] + string[-5] + string[-7]
         + string[-9] + string[-11]+ string[-13] + string[-15] + string[-17] + string[-19] + string[-21] + string[-23])
    return newString


print("tests for evenForward24(): ")
print(evenForward24("012345678901234567890123")) # returns 024680246802
print(evenForward24("O n l y E v e n N u m s ")) # return OnlyEvenNums


print("tests for alternatingReverse23(): ")
print(alternatingReverse23("01234567890123456789012")) # return 208642086420
print(alternatingReverse23("e s r e v e R r e t l A")) # return AlterReverse



