# Carmin Vuong
# hw41
# worked with no one
# advised by no one

# deficiencies that need fixing:
#   - add <p> and </p>
#   - instead of local variables, make a separate function that makes valid HTML
#   - add clear post-conditions and pre-conditions to each of the functions

def stackOfChars( lineOfChars):
    # pre-condition:
    # lineOfChars is a string of characters

    # post-condition:
    # returns html that allows most browsers to render as a column of characters, all inside a <p> tag

    HTMLsnippet = "  <p>"
    index = 0

    while index < len(lineOfChars):
        HTMLsnippet += lineOfChars[index] + "<br>"
        index += 1


    return  HTMLsnippet  + "</p>"



def makeValidHTML(title, body):
    # pre-condition: 
    # body and title are strings
    
    # post-condition:
    # returns valid HTML, putting "title" in the <title> tag and "body" in the <body> tag

    HTMLBeforeTitle = """<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset=utf-8>
    <title> """

    HTMLAfterTitle = """
     </title>
  </head>
  <body>
  """

    HTMLAfterBody = """
  </body>
</html>"""

    return HTMLBeforeTitle + title + HTMLAfterTitle + body + HTMLAfterBody


    


print(makeValidHTML("hw41", stackOfChars("Stuy") + '\n' + stackOfChars("1.6180339887")))
