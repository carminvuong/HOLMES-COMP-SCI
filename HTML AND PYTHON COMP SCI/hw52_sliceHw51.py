# Carmin Vuong
# hw52
# worked with no one
# advised by no one


print( 'task 3: four words')
MLK = 'I have a dream.'

# word 0
spaceIndex = MLK.find( ' ')
print( repr( MLK[0:spaceIndex] ))
MLK = MLK[spaceIndex + 1:len(MLK)]
# print( repr( MLK))

# copies of the code, to produce remaining words
# word 1
spaceIndex = MLK.find( ' ')
print( repr( MLK[0:spaceIndex] ))
MLK = MLK[spaceIndex + 1:len(MLK)]
# print( repr( MLK))

# word 2
spaceIndex = MLK.find( ' ')
print( repr( MLK[0:spaceIndex] ))
MLK = MLK[spaceIndex + 1:len(MLK)]
# print( repr( MLK))

# word 3
spaceIndex = MLK.find( ' ')

# no good! .find --> -1   Nobody wants that
spaceIndex = len( MLK)

# With the replacement value, the rest of
# the processing can remain unchanged.
print( repr( MLK[0:spaceIndex] ))
MLK = MLK[spaceIndex + 1:len(MLK)]

# expecting to have emptied MLK. Check that.
print( MLK == '')
print( '-'*8, end='\n'*2)
# --------

print( 'task 4: wordsFromPhrase')
def wordsFromPhrase( phrase):
    accum = ''
    while phrase:

        # Identify the position of the next space.
        spaceIndex = phrase.find(' ')
        # .find() returns -1 when not found. which is inconsistent
        # the the processing for earlier words. No one wants that.
        if spaceIndex == -1: spaceIndex = len( phrase)

        accum += phrase[0:spaceIndex] + '\n'
        phrase = phrase[spaceIndex+1:len(phrase)]
    return accum

# tests
text = 'I have a dream.'
wordsStack = \
'''I
have
a
dream.
'''
print( wordsFromPhrase( text))
print( wordsFromPhrase( text) == wordsStack)
print( '-'*8, end='\n'*2)

text = 'Life, Liberty and the pursuit of Happiness.'
wordsStack = "Life,\nLiberty\nand\nthe\npursuit\nof\nHappiness.\n"
print( wordsFromPhrase( text))
print( wordsFromPhrase( text) == wordsStack)
print( '-'*8, end='\n'*2)

text = 'they will not be judged by the color of their skin'
wordsStack = \
"""they
will
not
be
judged
by
the
color
of
their
skin
"""
print( wordsFromPhrase( text))
print( wordsFromPhrase( text) == wordsStack)
print( '-'*8, end='\n'*2)

text = 'but by the content of their character.'
wordsStack = \
"""but
by
the
content
of
their
character.
"""
print( wordsFromPhrase( text))
print( wordsFromPhrase( text) == wordsStack)
print( '-'*8, end='\n'*2)
