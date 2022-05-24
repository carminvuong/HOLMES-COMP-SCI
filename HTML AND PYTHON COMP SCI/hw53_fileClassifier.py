# Carmin Vuong
# hw53
# worked with Niki Chen
# advised by no one



def fileClassifier( filePath):
    fileExtension = ""
    for char in filePath:
        if char == ".":
            # .rfind() FINDS HIGHEST INDEX OF A CHARACTER, 
            # .lower() TURNS STRING INTO LOWERCASE 
            fileExtension = filePath[filePath.rfind("."):].lower() 
    if fileExtension == ".jpeg" or fileExtension == ".jpg":
        return "picture"
    elif fileExtension == ".mp3":
        return "music"
    elif fileExtension == ".nlogo":
        return "NetLogo"
    elif fileExtension == ".py":
        return "Python"
    else:
        return "ask the unhelpful file creator"

# print(fileClassifier("asdjhaiusdhja.PY")) # test case

print( fileClassifier( 'hw.py') == 'Python')
print( fileClassifier( 'StarSpangledBanner.Mp3') == 'music')
print( fileClassifier( 'Fred.mp3.JPEG.nlogo') == 'NetLogo')
print( fileClassifier( '') == 'ask the unhelpful file creator')
print( fileClassifier( 'nameWithoutSuffix') ==
                       'ask the unhelpful file creator'
                     )
