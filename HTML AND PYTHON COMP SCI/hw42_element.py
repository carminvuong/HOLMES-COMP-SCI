# Carmin Vuong
# hw42
# worked with no one
# advised by no one


def stackOfChars( lineOfChars):
    # Returns html that most browsers will render as a column of characters

    # precondition:
    # lineOfChars is the string of characters to be rendered
    stack = '<p>\n'
    pos = 0
    while pos < len( lineOfChars):
        stack += lineOfChars[ pos] + '<br>'
        pos += 1
    return stack + '\n</p>'

def element( tag, content):
    return "<" + tag + "> " + content + " </" + tag + ">"


def top( title):
    return '''<!DOCTYPE html>
              <html lang="en-US">
              ''' + \
                  element("head", '''
                  <meta charset=utf-8>
                  '''  + \
                      element("title", title)) + \
                '''
                <body>
           '''




# # -------------- test cases for element function ----------------
# print(element("p", "THIS IS SUPPOSED TO BE A PARAGRAPH"))
# print(element("ul", "THIS IS SUPPOSED TO BE AN UNORDERED LIST"))
# print(element("table", "THIS IS SUPPOSED TO BE A TABLE"))

print( top( 'element hw'))

print( stackOfChars( 'Stuy'))
# expecting code like http://davidmholmes.net/Stuy/2intro/hw/hw39_stackOfStuy.html

print( '\n <hr> \n') # to separate results visually

print( stackOfChars( '1.6180339887'))
# expecting code like http://davidmholmes.net/Stuy/2intro/hw/hw39_stackOfPhi.html