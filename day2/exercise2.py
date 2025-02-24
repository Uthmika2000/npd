#! /usr/bin/python

import sys

if len(sys.argv) != 2:
    print("[-] prog.py filename")
    exit(1)

fp = open(sys.argv[1], 'r')


a_set = ""
count = 0
original_txt = ""

print(format(0, "08x") + ": ", end="")

for line in fp:
    for c in line:
        hex_val = format(ord(c), "02x")
        #hex_val = hex(ord(c)).lstrip("02x").rstrip("L")
        a_set = a_set + hex_val
        count = count + 1
        
        if c.isprintable():
            original_txt = original_txt + c
        else:
            original_txt = original_txt + '.'

        if len(a_set) == 4:
            print(a_set, end=" ")
            a_set = ""
        if count % 16 == 0:
            print(" " + original_txt)
            original_txt = ""
            print(format(count, "08x") + ": ", end="")
       
if a_set:
    print(a_set, end=" ")
    print(original_txt)

print()
