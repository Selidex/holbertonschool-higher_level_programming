#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = "Last digit of"
ls = "and is less than 6 and not 0"
gf = "and is greater than 5"
if number < 0:
    i = -1
    number = number * -1
else:
    i = 1
if (number % 10) == 0:
    print("{} {} is 0 and is 0".format(ld, number * i))
elif number % 10 < 6 or i == -1:
    print("{} {} is {} {}".format(ld, number * i, (number % 10) * i, ls))
else:
    print("{} {} is {} {}".format(ld, number, number % 10, gf))
