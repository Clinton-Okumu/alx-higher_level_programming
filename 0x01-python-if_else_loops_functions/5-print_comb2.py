#!/usr/bin/python3
for number in range(100):
    print(str(number).zfill(2), end=' ')
    if number < 99:
        print(',', end='')
