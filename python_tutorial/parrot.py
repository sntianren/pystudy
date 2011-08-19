#!/usr/bin/env python
# Filename: parrot.py

def parrot(voltage, state = 'a stiff', action = 'voom'):
    print("-- This parrot wouldn't", action, end = ' ')
    print('if you put', voltage, 'volts through it.', end = ' ')
    print("E's", state, '!')
