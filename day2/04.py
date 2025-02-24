#! /usr/bin/python

import sys

if len(sys.argv) != 2:
    print("[-] prog.py filename")
    exit(1)

fp1 =  open(sys.argv[1], 'r')
fp2 = open(sys.argv[2], 'w')

for line in fp1:
    fp2.write(line)
