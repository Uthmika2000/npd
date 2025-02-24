#! /usr/bin/python
from threading import Thread
from time import sleep

def A():
    for i in range(20):
        print("*", end="")
        sleep(2)

def B():
    for i in range(20):
        print("#")
        sleep(1)

def C():
    for i in range(20):
        print("!!")
        sleep(1)

t1 = Thread(target=A, args=[])
t2 = Thread(target=B, args=[])
t3 = Thread(target=C, args=[])

t1.start()
t2.start()
t3.start()
