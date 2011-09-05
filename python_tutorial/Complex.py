#!/usr/bin/env python
# Filename: Complex.py

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

if __name__ == '__main__':
    x = Complex(3.0, -4.5)
    print((x.r, x.i))
