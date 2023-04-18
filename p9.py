#!/usr/bin/env python3

for a in range(1,1000):
    for b in range(a + 1 , 1000 - a + 1):
        c = 1000 - b - a
        if a**2 + b**2 > c**2:
            break
        elif a**2 + b**2 == c**2 and a + b + c == 1000:
            print(a,b,c, a*b*c)
            exit()
