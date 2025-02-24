#! /usr/bin/python

str2 = 'EFGH'

a = str1 + str2

print(a)

print(a.upper())
print(a.lower())
print(len(a))
print(len(str1))
print(len(str2))

print(a[4:])
print(a[:4])
print(a[::-1])

a = [1, 2, 4, 7, 5]
print(a)

a.sort()
print(a)

a.append('x')
print(a)

print(a.pop())
print(a)

a.insert(2, 'a')
print(a)

print(len(a))


a.remove(7)
print(a)


ages = {'a':11, 'b':10, 'c':33}
print(ages)
print(type(ages))

print(ages['b'])

"""
for i in range(0, 10, 2):
    print(i)

for i in [1, 2, 3]:
    print(i)
fp = open('03.py','r')

for l in fp:
    line = l.strip()
    for c in line:
        print(c)
"""

a = 10
i = 0
while (True):
#while (1):
    print(i)
    i=i+1
    if (i == 5):
        break

while a > 5 :
    print(a)
    a=a-1


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

while True:
    x = input("Value :")
    print(x)

void main(){
	printf("Hello World\n");
}
