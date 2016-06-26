# !/usr/bin/python -tt
# -*- coding: utf-8 -*-
'''
Chandu and Consecutives Letters
'''

T = int(raw_input())

for i in range(T):
    S = raw_input()

    longitud = len(S)
    sol = S[0]

    for l in range(1, longitud):
        if S[l-1] != S[l]:
            sol = sol + S[l]
    print sol
