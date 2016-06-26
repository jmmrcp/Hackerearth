#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

texto = raw_input("Data: \n")
sol = ""

for letra in texto:

    if letra.islower():
        sol += letra.upper()
    if letra.isupper():
        sol += letra.lower()
print sol
