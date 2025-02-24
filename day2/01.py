#! /usr/bin/python
import sys

#print("Number of args:" , end="")
#print(len(sys.argv))

#print(sys.argv)
#print(type(sys.argv))

if len(sys.argv) != 2:
    print("[-] incorrect input")
    exit(1)

for arg in sys.argv:
    print(arg)
