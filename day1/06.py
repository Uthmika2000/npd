#! /usr/bin/python
import time

i=0
try:
    while (True):
        print(i)
        i+=1    # i = i+1
        time.sleep(1)
        try:
            if i == 5:
                print(i/0)
        except Exception as e:
            print("Exception : ", end="")
            print(e)
            continue
except KeyboardInterrupt as e:
    print(e)
    print("[-] Terminating")
except  Exception as e:
    print(e)
