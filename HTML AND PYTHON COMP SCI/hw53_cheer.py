# Carmin Vuong
# hw53
# worked with Niki Chen
# advised by no one


def cheer( phrase):
    finalCheer = ""
    for char in phrase:
        if char == " ":
            finalCheer += "Gimme a space, the final frontier" + "\n"
        elif char == "\n":
            finalCheer += "Gimme a newline" + "\n"
        else: 
            finalCheer += "Gimme a " + repr(char) + "\n"
    return finalCheer

# tests
seek = "Gimme a 'C'\nGimme a 'S'\n"
print( seek)
cheerResult = cheer('CS')
print( cheerResult)
print( cheerResult == seek, end='\n'*2)

# Handle a space.
# Python concatenates adjacent string literals.
seek = "Gimme a 'C'\nGimme a 'S'\n"           \
       "Gimme a space, the final frontier\n"  \
       "Gimme a 'a'\nGimme a 't'\n"
print( seek)
cheerResult = cheer('CS at')
print( cheerResult)
print( cheerResult == seek, end='\n'*2)

#handle a newline
seek = "Gimme a 'C'\nGimme a 'S'\n"           \
       "Gimme a space, the final frontier\n"  \
       "Gimme a 'a'\nGimme a 't'\n"           \
       "Gimme a newline\n"                    \
       "Gimme a 'S'\nGimme a 't'\nGimme a 'u'\nGimme a 'y'\n"
print( seek)
cheerResult = cheer('CS at\nStuy')
print( cheerResult)
print( cheerResult == seek, end='\n'*2)
