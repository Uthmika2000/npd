#! /usr/bin/python

sum = 0

while True:
    try:
        x = input("Value :")
    except KeyboardInterrupt:
        print(x)
        continue
    
    if x == "0":
        break
    # elif isinstance(x, (int, float)):
    try:
        y = float(x)
    except (ValueError,KeyboardInterrupt):
        print(x)
        continue
    sum = sum + y

print(sum)
