# /usr/bin/python -tt
# -*- coding: utf-8 -*-

'''
'''

N = int(raw_input())
solucion = 1

for numero in range(1, N+1):
    print numero
    solucion *= numero
print solucion
