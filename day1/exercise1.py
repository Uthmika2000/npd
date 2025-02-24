#! /usr/bin/python

sum = 0

while True:
    x = input("Value :")
    
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
