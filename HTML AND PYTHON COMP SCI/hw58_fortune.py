#! /usr/bin/python3

# Carmin Vuong
# hw58
# worked with Niki Chen
# advised by no one

import random

print("content-type: text/html")
print()


fortunesList = [
    "The CS test this Friday will be postponed and moved to next Friday.",
    "Exactly one year from now, something spectacular will happen.",
    "You will get a perfect score on your next test!",
    "You will fail miserably on your next test. Better luck next time!",
    "You will be accepted into all of your electives.",
    "You will ace the next algebra test that you will take.",
    "In exactly 5 years, you will be 5 years older than you are now.",
    "Mr. Holmes will curve the next CS test."
]

# ---------- TESTING CODE -------------
# for counter in range(len(fortunesList)*5):
#     print(random.choice(fortunesList))

print('''<!DOCTYPE html>
<html lang="en">

<head>
<meta charset=utf-8>
<title>hw58: fortune telling </title>
</head>

<body> <p>''')

print("<strong>I know your fortune! Here it is: <br></strong>")
print(random.choice(fortunesList))

print('''</p></body>

</html>''')