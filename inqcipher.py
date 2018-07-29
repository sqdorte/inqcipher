#!/usr/bin/python3
# -*- coding:utf-8 -*-

from random import randint

def shift(l, n):
    return l[n:] + l[:n]

def generate_wheel(chars, levels, s=True):
    size = len(str(levels * len(chars)))

    wheel = []
    for x in range(levels):
        wheel.append(['0' * (size - len(str(n+x*len(chars)))) + str(n+x*len(chars)) for n in range(1, len(chars)+1)])

    if s:
        for x in range(len(wheel)-1):
            wheel[x] = shift(wheel[x], randint(0, len(chars)-1))

    return wheel

def generate_key(chars, wheel):
    index = randint(0, len(chars))
    key = chars[index]

    for w in wheel:
        key += w[index]
    
    return key

def decrypt_key(chars, key, levels):
    size = len(str(levels * len(chars)))
    index = chars.index(key[0])
    wheel = generate_wheel(chars, levels, s=False)
    
    for x in range(len(wheel)-1): # EU TENHO Q MELHORAR ISSO TAMBÉM desculpa
        while True:
            wheel[x] = shift(wheel[x], 1)
            if wheel[x][index] == [key[1:][m:m+size] for m in range(0, len(key)-2, size)][x]:
                break

    return wheel

def encrypt(plain_text, wheel, chars):
    levels = len(wheel)
    ciphered = ''

    for char in plain_text:
        ciphered += wheel[randint(0, levels-1)][chars.index(char)]

    return ciphered

def decrypt(ciphered, wheel, chars):
    levels = len(wheel)
    size = len(str(levels * len(chars)))
    plain_text = ''

    for char in [ciphered[x:x+size] for x in range(0, len(ciphered), size)]:
        for x in wheel:
            if char in x:
                w = x

        plain_text += chars[w.index(char)]

    return plain_text