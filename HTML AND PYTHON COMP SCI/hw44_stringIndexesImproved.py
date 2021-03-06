# Carmin Vuong
# hw43
# worked with no one
# advised by no one


def stackOfChars( lineOfChars):
    # Returns html that most browsers will render as a column of characters

    # precondition:
    # lineOfChars is the string of characters to be rendered
    stack = ''
    pos = 0
    while pos < len( lineOfChars):
        stack += lineOfChars[ pos] + '<br>'
        pos += 1
    return element( 'p'
                  , stack + '\n'
                  )

def element( tag, content, attrib=''):
   # Return valid html with a start tag, the contents,
   # any attributes, and the end tag.
   return   '<' + tag + ' ' + attrib + '>'  \
          + content  \
          + '</' + tag + '>'

def headEl( title):
    # Return html for a head element with the given "title"
    return  element( 'head'
                   ,   '<meta charset=utf-8> \n'
                     + element( 'title', title) + element("style", """
       table {
         border: 2px solid DeepSkyBlue;
         border-collapse: collapse;
         }
       th,
       td {
         border: 1px solid DeepSkyBlue;
         padding: 5px;
         }
     """)
                   )

newLine = "\n"

def makeTableOfIndexes(string):
    # accepts a string
    # returns a table containing each character in "string" and their respective valid indexes

    tableBody = ""
    negIndex = -len(string)

    while negIndex <= -1:
        tableBody += indexedCharsRow(negIndex, string[negIndex]) + newLine
        negIndex += 1

    posIndex = 0
    while posIndex < len(string):
        tableBody += indexedCharsRow(posIndex, string[posIndex]) + newLine
        posIndex += 1

    return element("table", 
            "\n" + element("tbody", tableBody))

def indexedCharsRow(index, char):
    # accepts an integer as "index", and a single-character string as "char"
    # returns a single row of a table, with 'index' in column 0 and 'char' in column 1

    return element("tr", element("td", str(index)) +  element("td", char))
    

# # test element
# print( element( 'tagName', 'contents', 'attributes'))

print( '<!DOCTYPE html>')  # kept separate because doctype is not html
print( element( 'html'
              , '\n'
                + headEl( 'element hw')
                + '\n'
                + element( 'body'
                         , makeTableOfIndexes("Stuy") + "\n<hr>\n" + 
                         makeTableOfIndexes("Carmin") + "\n<hr>\n" + 
                         makeTableOfIndexes("H")
                         )
              , 'lang="en-US"'   # attribute for <html> tag
              )
     )

# # test indexedCharsRow
# print(indexedCharsRow(-1, "a"))


