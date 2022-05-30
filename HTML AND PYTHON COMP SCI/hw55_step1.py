# Carmin Vuong
# hw55
# worked with Niki Chen
# advised by no one

# ----------- DELIVERABLES -------------
# - replace "you" with "ye"  [DONE]
# - replace "myself" with "meself" [DONE]
# - replace "your" with "yers" [DONE]
# - replace "of" with "o'" [DONE]
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
    newString = newString.replace(" of ", " o' ")
    newString = newString.replace(" Of ", " O' ")
    return newString


print(pirateSpeak(" You yourself you "))
print(pirateSpeak(" Myself myselfnessij myself "))
print(pirateSpeak(" your Yourne Your "))
print(pirateSpeak(" Of ofcourse of  of "))


print(pirateSpeak('''Sorry to disappoint you and all that,
but the greatest wizard in the world is
Albus Dumbledore. Everyone says so. Even
when you were strong, you didn't dare try
and take over at Hogwarts. Dumbledore saw
through you when you were at school and he
still frightens you now, wherever you're hiding
these days.'''))

#  Ye yourself ye 
#  Meself myselfnessij meself 
#  yers Yourne yers
#  O' ofcourse o'  o'
# Sorry to disappoint ye and all that,
# but the greatest wizard in the world is
# Albus Dumbledore. Everyone says so. Even
# when ye were strong, ye didn't dare try
# and take over at Hogwarts. Dumbledore saw
# through ye when ye were at school and he
# still frightens ye now, wherever you're hiding
# these days.
    
    


