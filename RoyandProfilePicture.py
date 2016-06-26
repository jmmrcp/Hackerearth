# /usr/bin/python -tt
# -*- coding: utf-8 -*-

'''
'''

l = int(raw_input())  # Dimensiones minimas de la imagen
n = int(raw_input())  # Numero de imagenes a procesar

for imagenes in range(n):
    data = map(int, raw_input().split())
    w, h = data

    if w < l or h < l:
        print "UPLOAD ANOTHER"
    elif w == h:
        print "ACCEPTED"
    else:
        print 'CROP It'
