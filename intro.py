import math


def parity(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


def prime(num):
    y = num
    while y > 0:
        y -= 1
        # first check if num is 1 cuz 1 != prime
        # then check if y > 1 cuz if it's 1 it num would be prime
        # then get the reminder of num / y cuz if its 0, its not prime
        if num == 1 or y > 1 and num % y == 0:
            print("not prime")
            break
        elif y == 1:
            print("prime")


def fibonacci(length):
    x = 0
    y = 1
    while length > 0:
        length -= 1
        print(x)
        # parity(x)
        # prime(x)
        x += y
        y = x-y


length = 20
fibonacci(length)
