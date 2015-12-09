'''
Created on 9 Dec 2015

@author: Harry
'''

def ASCII_Input():
    try:
        while True:
            data=raw_input()
            if not data: break
            yield data
    except KeyboardInterrupt:
        return

print 'Please enter the entire ASCII:'
ASCII = list(ASCII_Input())

print 'AsciiArt = ',
print ASCII

print 'for line in AsciiArt: print line'

print 'Copy both the list and the for loop that are printed in the two lines above this one into your program.'
print 'Place the list wherever you want then place the loop wherever you want the ASCII to be printed'
    
    

