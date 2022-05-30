# Carmin Vuong
# hw56
# worked with Niki Chen
# advised by no one

# ----------- DELIVERABLES -------------
# - replace "you" with "ye"  [DONE]
# - replace "myself" with "meself" [DONE]
# - replace "your" with "yers" [DONE]
# - replace "of" with "o'" [DONE]
# - replace "for" with "fer" [DONE]
# - replace "the" with "t'" [DONE]
# - add an exclamation point to all sentences [DONE]
# - replace words that end in "ing" with "in'" [DONE]
# - replace "I", "my", "mine" with "me" [DONE]
# - replace "am", "is", "are", or words with "'re" with "be" [DONE]
# - add "Arrr!"" after every other sentence. [DONE]


# ---------- description and how the code works -------------

# The main function of my code pirateSpeak() works by splitting a string into separate words, using .split(). I used a
# for loop to iterate through the list, using if statements to differentiate between words with and without punctuation. 
# There are also some special cases that need to be accounted for in this function. Each time the loop is run, the
# function pirateWord() is called. It is a function that returns a word's corresponding pirate-version, abiding by the translation
# rules. For each rule, pirateWord() invokes changeWithCapitilization(), which is a function that changes the word to its 
# pirate-version, accounting for capitilization. To differentiate between words with and without punctuation, I made the 
# hasPunctuation() function which returns True if there is punctuation in the string. For the "Arrr!" translation rule, I made a 
# separate function called arrr(). It works by first finding the indexes of all exclamation points (which marks the end
# of a sentence), which is done by the findAllIndexes() function. To find every other index, I used range() with a step of 2.
# I iterated through every character of the piratedString and if the index matched the index of every other exclamation mark,
# the string " Arrr!" is added.


def hasPunctuation(string):
    # precondition: takes a string
    # postcondition: returns True if there is punctuation in string (question marks, periods, exclamation marks)
    #                returns False otherwise

    punctuationList = [".", "!", "?"]
    for punctuation in punctuationList:
        if punctuation in string:
            return True
    return False


def changeWithCapitalization(wordToBeChanged, desiredWord):
    # precondition: takes 2 strings, "wordToBeChanged" needs to at least one character
    # postcondition: returns "desiredWord" with capitilization that matches "wordToBeChanged"

    if wordToBeChanged == "I":
        return desiredWord.casefold()

    elif wordToBeChanged.isupper():
        return desiredWord.upper()

    elif wordToBeChanged.islower():
        return desiredWord.casefold()

    elif wordToBeChanged[0].isupper():
        return desiredWord.title()

    return wordToBeChanged


def pirateWord(word):
    # precondition: takes a string
    # postcondition: returns its pirate - version according to the translation rules 

    if word.casefold() == "you":
        return changeWithCapitalization(word, "ye")
    elif word.casefold() == "myself":
        return changeWithCapitalization(word, "meself")
    elif word.casefold() == "your":
        return changeWithCapitalization(word, "yers")
    elif word.casefold() == "of":
        return changeWithCapitalization(word, "o'")
    elif word.casefold() == "for":
        return changeWithCapitalization(word, "fer")
    elif word.casefold() == "the":
        return changeWithCapitalization(word, "t'")
    elif word.casefold() in ["i", "my", "mine"]:
        return changeWithCapitalization(word, "me")
    elif word.casefold() in ["am", "is", "are"]:
        return changeWithCapitalization(word, "be")
    elif word[-3:] == "ing":
        return changeWithCapitalization(word, word[:-3] + "in'") 
    elif word[-3:] == "'re":
        return changeWithCapitalization(word, word[:-3]) + " be"
    else:   # normal characters
        return word

def findAllIndexes(desiderata, string):
    # precondition: takes 2 strings
    # postcondition: returns a list containing all the indexes where "desiderata" appear in "string"

    indexes = []
    for index, char in enumerate(string):
        if char == desiderata:
            indexes.append(index)
    return indexes

def arrr(string):
    # precondition: takes a string
    # postcondition: returns a new string with "Arrr!" after every other sentence in "string"

    finalString = ""
    allIndexes = findAllIndexes("!", string)
    everyOther = []

    for index in range(1, len(allIndexes), 2):
        everyOther.append(allIndexes[index])

    for index, char in enumerate(string):
        if index in everyOther:
            finalString += char + " Arrr!"
        else:
            finalString += char
    return finalString

def pirateSpeak(string):
    # precondition: takes a string
    # postcondition: returns a new string with all of the pirate translation rules applied

    piratedString = ""
    space = " "

    for index, word in enumerate(string.split()):
        if hasPunctuation(word):
            piratedString += pirateWord(word[:-1]) + "!" + space
        elif "," in word:
            piratedString += pirateWord(word[:-1]) + "," + space
        elif word == "I" and hasPunctuation(string.split()[index - 1]):
            piratedString += "Me" + space
        else:
            piratedString += pirateWord(word) + space

    return arrr(piratedString[:-1])

# ------------ TEST CASES --------------

print( pirateSpeak('You yourself you.'))  #Ye yourself ye!
print( pirateSpeak('Your your yourself your.'))  #Yers yers yourself yers!
print( pirateSpeak('The the theme the.'))  #T' t' theme t'!
print( pirateSpeak('Thing flinging king'))  #Thin' flingin' kin'
print( pirateSpeak('I I, I. My my my. Mine mine mine.'))  #Me me! Me me me! Me me me!
print( pirateSpeak("Am am am. Is is is. Are are are. They're you're.")) # Be be be! Be be be! Be be be! They be you be
print( pirateSpeak("Myself myself myself."))  #Meself meself meself!
print( pirateSpeak("For for for."))  #Fer fer fer!

print(pirateSpeak("You YOU you, Your YOUR the The your. They're you're You're singing dings RINGING? I me Mine, I for For of Of!"))
# Ye YE ye, Yers YERS t' T' yers! They be you be You be singin' dings RINGING! Arrr! Me me Me, me fer Fer o' O'!

print(pirateSpeak("I am your you myself Tho. The of?") == "Me be yers ye meself Tho! T' o'! Arrr! ")

print(pirateSpeak("I AM you, myself IS mine, yourself is YOUR, the king. The Arrr should be in the next sentence, of course. \
You're going to be singing and they are yours."))
#Me BE ye, meself BE me, yourself be YERS, t' kin'! T' Arrr should be in t' next sentence, o' course! Arrr! You be goin' to be singin' and they be yours!