#!/usr/bin/env python2
# Filename: break.py

while True:
    s = raw_input('Enter something: ')
    if s == 'quit':
        break
    print 'Length of the string is', len(s)

print 'Done'
