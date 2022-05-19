# Carmin Vuong
# hw51
# worked with no one
# advised by no one


def slice( input, startAt, stopBefore):
     #precondition: The parameter "input" must be a string of text
    #postcondition: Return a sub-string of the string input starting with the
    #               character at position startAt
    #               and extending up to and not including the character
    #               at position stopBefore
    pos = startAt
    newString = ''
    while pos < stopBefore:
        newString += input[pos]
        pos += 1
    return newString

spaceTrouble = " string with hard-to-see surrounding spaces   "

print( spaceTrouble)  # It's hard to see surrounding spaces that are printed

spaceVisible = repr( spaceTrouble)
print( spaceVisible)  # A string REPResentation of that string helps.

print( '-' * 25)

newlineTrouble = '''
newlines
are whitespace, too  
'''
print( newlineTrouble)  # Printed newlines confuse me.

newlinesVisible = repr( newlineTrouble)
print( newlinesVisible) # A string REPResentation of that string helps.
print( '-' * 50)


#           012345678901234567
sentence = "My name is Carmin."
print(repr(slice(sentence, 0, sentence.find(" "))))

sentence = slice(sentence, 3, len(sentence))
print(repr(slice(sentence, 0, sentence.find(" "))))

sentence = slice(sentence, 5, len(sentence))
print(repr(slice(sentence, 0, sentence.find(" "))))

sentence = slice(sentence, 3, len(sentence))
print(repr(sentence))

print("-" * 25)

def wordsFromPhrase(phrase):
    verticalList = ""

    while phrase.find(" ") != -1:
        verticalList += repr(slice(phrase, 0, phrase.find(" "))) + "\n"
        phrase = slice(phrase, phrase.find(" ") + 1, len(phrase))
    return verticalList + repr(phrase)

#--------------------- test cases -------------------------
print(wordsFromPhrase( 'Life, Liberty and the pursuit of Happiness.') == \
    "'Life,'\n'Liberty'\n'and'\n'the'\n'pursuit'\n'of'\n'Happiness.'")
    
print("-" * 25)

print(wordsFromPhrase("Execute the statements in the function, using the copied values.") == \
    "'Execute'\n'the'\n'statements'\n'in'\n'the'\n'function,'\n'using'\n'the'\n'copied'\n'values.'")

print("-" * 25)

print(wordsFromPhrase("Long ago, the four nations lived together in harmony.") == \
    "'Long'\n'ago,'\n'the'\n'four'\n'nations'\n'lived'\n'together'\n'in'\n'harmony.'")


