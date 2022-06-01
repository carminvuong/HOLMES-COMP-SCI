# Carmin Vuong
# hw57
# worked with no one
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
        # Arrr! after every other sentence
    # programming improvements
        # Replace stubs with effective code.

# work beyond expectations
    # Use a list of lists.


# Combine input lines into a single normalized string
def unify( phrase):
    # temp for debugging
    print( 'in unify, phrase.strip()='
         , repr( phrase.strip())
         , end='\n'*2
         )

    return phrase.strip().replace('\n',' ')

# return a list of sentences, each a list of words
def sentencesList( phrase):
    sentenceS = unify( phrase).split('.')
    # temp for debugging
    print( 'in SentencesList(), sentenceS='
         , repr( sentenceS)
         , end='\n'*2
         )

    # Remove null sentences. I *think* .split puts 1
    # after the last period. But others might exist.
    nullSentence = ''
    while nullSentence in sentenceS:
        sentenceS.remove( nullSentence)

    # Split each sentence into a list of words.
    sentsOfWords = []
    for sentence in sentenceS:
        sentsOfWords.append( sentence.split());

    return sentsOfWords


# Translate individual words to pirate speech.
# Maintain capitalization.
def translate( sentencesOfWords):
    # stub; Someday implement using a dictionary.
    return( sentencesOfWords)


# Add "Arrr" as every other sentence.
def arrrify( sentencesOfWords):
    newSentencesOfWords = []
    for sentence in sentencesOfWords:
        newSentencesOfWords.append(sentence)
        newSentencesOfWords.append(["MRHOLMES"])
    return( newSentencesOfWords)


def piratify( phrase):
    sentencesOfWords = sentencesList( phrase)
    # temp for debugging
    print( 'in piratify, sentencesList()='
         , repr( sentencesOfWords)
         , end='\n'*2
         )

    translation = translate( sentencesOfWords)
    arrrification = arrrify( translation)

    # Combine each sentence into the rephrased speech.
    rephrasing = ''
    for sentence in sentencesOfWords:
        rephrasing += ' '.join( sentence) + '! '

    return rephrasing

hagrid = '''
Sorry to disappoint you and all that,
but the greatest wizard in the world is
Albus Dumbledore. Everyone says so. Even
when you were strong, you didn't dare try
and take over at Hogwarts. Dumbledore saw
through you when you were at school and he
still frightens you now, wherever you're hiding
these days.'''

print( '', 'As spoken on the Spanish Main:'
     , piratify( hagrid)
     , sep='\n'
     , end='\n' + '-'*32 + '\n'*2
     )
