# Carmin Vuong
# hw54
# worked with Niki Chen
# advised by no one

# ----------- DELIVERABLES -------------
# - replace "you" with "ye"  [DONE]
# - replace "myself" with "meself" [DONE]
# - replace "your" with "yers" [DONE]
# - replace "of" with "o'"
# - replace "for" with "fer"
# - replace "you" with "ye"
# - add an exclamation point to all sentences
# - replace words that end in "ing" with "in'"
# - replace "I", "my", "mine" with "me"
# - replace "am", "is", "are", or words with "'re" with "be"
# - add "Arrr!"" after every other sentence.



def pirateSpeak(string):
#     pirateString = ""
# #                     0123456789012345678901234567890123456789012345678901234567890123456789                       
#     toBeTranslated = "you    You    myself Myself your   Your   of     Of     "
#     translatedWords = "ye    Ye     meself Meself yers   Yers   o'     O'     "
    
#     space = " "
#     for word in string.split():
#         return "stub"
    newString = ""
    newString = string.replace(" You ", " Ye ")
    newString = newString.replace(" you ", " ye ")
    newString = newString.replace(" Myself ", " Meself ")
    newString = newString.replace(" myself ", " meself ")
    newString = newString.replace(" Your ", " yers ")
    newString = newString.replace(" your ", " yers ")
    return newString


print(pirateSpeak(" You yourself you "))
print(pirateSpeak(" Myself myselfnessij myself "))
print(pirateSpeak(" your Yourne Your "))


print(pirateSpeak('''Sorry to disappoint you and all that,
but the greatest wizard in the world is
Albus Dumbledore. Everyone says so. Even
when you were strong, you didn't dare try
and take over at Hogwarts. Dumbledore saw
through you when you were at school and he
still frightens you now, wherever you're hiding
these days.'''))
    
    


