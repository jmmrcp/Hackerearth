# /usr/bin/python -tt
# -*- coding: utf-8 -*-

'''
'''

lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

N = int(raw_input())

while N > 0:
    digito = N % 10
    lista[digito] += 1
    N /= 10

for i in range(10):
        print i, lista[i]
