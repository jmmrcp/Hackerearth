#! /usr/bin/env python
# -*- coding: utf-8 -*-

python_command=u'/usr/bin/env python'
encoding='utf-8'


'''
PuchiandLuggage.py - v0.1 24/06/2016 Jose Martínez


Hackereath -> Code Monk (Sorting)
'''

__author__ = 'Jose Martinez'
__copyright__ = 'Copyright 2016, Computerwizards'
__license__ = 'GPL'
__version__ = '0.1'
__date__ = '24-06-2016'
__maintainer__ = 'Jose Martinez'
__email__ = 'jmmrcp@gmail.com'
__status__ = 'Production'

# Copyright © 2016, José Martínez Ruiz.
#
# Esta programa es software libre; se puede redistribuir y/o modificar conforme
# las disposiciones de la Licencia Pública General GNU, tal como está publicada
# por la Free Software Foundation; versión 2 de la licencia, o también (a su
# elección) toda versión posterior.
#
# Este programa es distribuido con la esperanza de que sea útil, pero
# SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de COMERCIALIZACIÓN
# o de ADAPTACIÓN A UN OBJETIVO EN PARTICULAR. Para más detalles, ver la
# Licencia Pública General GNU.


# LANG=es


def _test():
    import doctest
    doctest.testmod()


def main():
    numerodecasos = int(raw_input())

    for t in range(numerodecasos):
        numerodeamigos = int(raw_input())
        listadepesos = []
        solucion = []

        for n in range(numerodeamigos):
            peso = int(raw_input())
            listadepesos.append(peso)
            listaordenada = sorted(listadepesos)

        for maleta in listadepesos:
            posicion = listaordenada.index(maleta)
            solucion.append(posicion)
            listaordenada.remove(maleta)

        print " ".join(map(str, solucion))




if __name__ == '__main__':
    main()
