# Carmin Vuong
# hw39
# worked with no one
# advised by no one

def stackOfChars( lineOfChars):

    validHTMLbeginning = """<!DOCTYPE html>
<html  lang="en-US">
  <head>
    <meta charset=utf-8>
    <title> minimal </title>
  </head>
  <body>
  """

    validHTMLend = """
  </body>
</html>"""

    HTMLsnippet = ""
    index = 0

    while index < len(lineOfChars):
        HTMLsnippet += lineOfChars[index] + "<br>"
        index += 1


    return validHTMLbeginning + HTMLsnippet + validHTMLend


print( stackOfChars( 'Stuy'))
# expecting code like http://davidmholmes.net/Stuy/2intro/hw/hw39_stackOfStuy.html

print( '\n', '-' * 50, '\n') # to separate results visually

print( stackOfChars( '1.6180339887'))
# expecting code like http://davidmholmes.net/Stuy/2intro/hw/hw39_stackOfPhi.html