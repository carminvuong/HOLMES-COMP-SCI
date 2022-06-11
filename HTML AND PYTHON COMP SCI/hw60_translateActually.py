# Carmin Vuong
# hw59
# worked with Niki Chen
# advised by no one


# goals accomplished
    # Starting with plain text,
    # create a list of sentences,
    # each of which is a list of words.
    # Stubs for...
        # o  translating words
        # o  inserting "Arrr" sentences
    # Convert sentences of words back into plain text.
        # Exclamation point at the end of each sentence.
    # Arrr! after every other sentence

# goals not yet accomplished
    # known bugs
    # translate words
        # you --> ye
        # your --> yers
        # the --> t'
        # of --> o'
        # words that end with ing --> in'
        # I, my, mine --> me
        # am, is, are, 're --> be
        # myself --> meself
        # for --> fer
# work beyond expectations
    # Use a list of lists.


# ---------- translation dictionary ------------
translationDict = {
        "you":"ye",
        "your":"yers",
        "the":"t'",
        "i":"me",
        "my":"me",
        "mine":"me",
        "am":"be",
        "is":"be",
        "are":"be",
        "myself":"meself",
        "for":"fer",
        }

# Combine input lines into a single normalized string
def unify( phrase):
    # # temp for debugging
    # print( 'in unify, phrase.strip()='
         # , repr( phrase.strip())
         # , end='\n'*2
         # )

    return phrase.strip().replace('\n',' ')

# return a list of sentences, each a list of words
def sentencesList( phrase):
    sentenceS = unify( phrase).split('.')
    # # temp for debugging
    # print( 'in SentencesList(), sentenceS='
         # , repr( sentenceS)
         # , end='\n'*2
         # )

    # Remove null sentences. I *think* .split puts 1
    # after the last period. But others might exist.
    nullSentence = ''
    while nullSentence in sentenceS:
        sentenceS.remove( nullSentence)

    # Split each sentence into a list of words.
    sentsOfWords = []
    for sentence in sentenceS:
        sentsOfWords.append( sentence.split())

    return sentsOfWords


# Translate individual words to pirate speech.
# Maintain capitalization.
def translate( sentencesOfWords):
    # stub; Someday implement using a dictionary.

    # # temp for debugging
    # print( 'in translate, initial sentencesOfWords-->'
         # , repr( sentencesOfWords)
         # , end='\n'*2
         # )

    return( sentencesOfWords)


# Add "Arrr" as every other sentence.
def arrrify( sows):  # "sows" got too long
    # For the pattern of where Arrrs are needed,
    # see Piazza@370

    # Insert Arrrs starting at the end of the text,
    # working back towards the beginning . That way,
    # an insert leaves unchanged the subscripts
    # at which subsequent inserts occur.

    insertAt = len( sows) - len( sows) % 2
      # maps even int --> itself
      #      odd int --> the next lower even int
    while insertAt > 0:  # no Arrr at beginning
        sows.insert( insertAt, ['Arrr'])
        insertAt -= 2
    return( sows)


def piratify( phrase):
    sentencesOfWords = sentencesList( phrase)
    # # temp for debugging
    # print( 'in piratify, sentencesList()='
         # , repr( sentencesOfWords)
         # , end='\n'*2
         # )

    translation = translate( sentencesOfWords)
    arrrification = arrrify( translation)

    # Combine each sentence into the rephrased speech.
    rephrasing = ''
    for sentence in sentencesOfWords:
        rephrasing += ' '.join( sentence) + '! '

    return rephrasing


def rankAndFile( fileCount, rankCount):
    finalString = ""
    for file in range(fileCount):
        finalString += "file " + str(file) + "\n"
        for rank in range(rankCount):
            finalString += "    rank " + str(rank) + '\n'

    return finalString


# ----------- test cases for rankAndFile() --------------
print(rankAndFile( 2, 3),'\n','-'*10)
print(rankAndFile( 1, 4),'\n','-'*10)
print(rankAndFile( 5, 0),'\n','-'*10)
print(rankAndFile( 0, 3),'\n','-'*10)

# test arrrify()
# print( '', 'arrrify an even number of sentences'
#      , piratify( 'Sentence 0. Sent 1. Sent 2. Sent 3. Sent 4. Sent 5.')

#      , 'arrrify an odd number of sentences'
#      , piratify( 'Sentence 0. Sent 1. Sent 2. Sent 3. Sent 4.')

#      , 'arrrify edge case'
#      , piratify( 'Too short to bother.')

#      , sep='\n'
#      , end='\n' + '-'*32 + '\n'*2
#      )


harry = '''
Sorry to disappoint you and all that,
but the greatest wizard in the world is
Albus Dumbledore. Everyone says so. Even
when you were strong, you didn't dare try
and take over at Hogwarts. Dumbledore saw
through you when you were at school and he
still frightens you now, wherever you're hiding
these days.'''
# _Chamber of Secrets_, chapter 17

print( '', 'Harry on the Spanish Main:'
     , piratify( harry)
     , sep='\n'
     , end='\n' + '-'*32 + '\n'*2
     )
