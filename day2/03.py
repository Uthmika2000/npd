#! /usr/bin/python

import sys

if len(sys.argv) != 2:
    print("[-] prog.py filename")
    exit(1)

fp =  open(sys.argv[1], 'r')

for line in fp:
    #print(line,end="")
    for c in line:
        print(c,end="")
