#!/usr/bin/env python

# doc string
"this is a test module"

# import
import sys
import os

# (global) variable
debug = True

# class def
class FooClass (object) :
    "Foo class"

    pass

# func def
def test () :
    "test function"
    foo = FooClass()

    if debug :
        print ( 'ran test()' )

# main
if __name__ == '__main__' :
    test()
