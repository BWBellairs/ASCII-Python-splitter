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

print ASCII

print 'Copy that into your program and use a for loop to print each item in the list on a new line. Your ASCII will be printed correctly.'
    
    

