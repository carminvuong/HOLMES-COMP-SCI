# Carmin Vuong
# hw52
# worked with no one
# advised by no one



#    0123456
s = 'abcdefg'

# Sample answer:
# s[1:4] is the slice of the string bound to s
# starting at position 1
# stopping before position 4
print( s[1:4] == 'bcd')

print( len(s)           == 7)

# s[1:len(s)] is the slice of the string bound to s
# starting at position 1    
# stopping before position 7
print( s[1:len(s)]      == 'bcdefg')

# s[1:len(s) * 20] is the slice of the string bound to s
# starting at position 1
# stopping before position 140
print( s[1:len(s) * 20] == 'bcdefg')

# s[3:3] is the slice of the string bound to s
# starting at position 3
# stopping before position 3
print( s[3:3]           == '')

# s[1:-1] is the slice of the string bound to s
# starting at position 1
# stopping before -1
print( s[1:-1]          == 'bcdef')

# s[:3] is the slice of the string bound to s
# starting at position 0
# stopping before position 3
print( s[:3]            == 'abc')

# s[3:] is the slice of the string bound to s
# starting at position 3
# stopping before position 7
print( s[3:]            == 'defg')


split = 5 # better: change this to your fav integer
#  For any value of "split", s[:split] + s[split:] is 
# the slice of the string bound to s
# starting at position 0
# stopping before position 7
print( s[:split] + s[split:] == 'abcdefg')


# s[:] is the slice of the string bound to s
# starting at position 0
# stopping before position 7
print( s[:] == 'abcdefg')


 #    0123456
#s = 'abcdefg'
# The third value is called the "stride".
# s[1:6: 2] is the slice of the string bound to s
# starting position 1
# stopping before position 6
print( s[1:6: 2] == 'bdf')

# s[6:1:-1] is the slice of the string bound to s
# starting at position 6
# stopping before position 1
print( s[6:1:-1] == 'gfedc')

# s[::-1] is the slice of the string bound to s
# starting ??
# stopping ??
print( s[::-1]   == 'gfedcba')

