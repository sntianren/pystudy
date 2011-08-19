#!/usr/bin/env python
# Filename: write_multiple_items.py

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
