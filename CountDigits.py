# /usr/bin/python -tt
# -*- coding: utf-8 -*-

'''
'''

lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def divInDigits(numero):
    '''

    '''

    while numero > 0:
        digito = numero % 10
        CountDigits(digito)
        numero /= 10

    imprimeResultado()


def CountDigits(numero):
    '''

    '''
    lista[numero] += 1


def imprimeResultado():
    for i in range(10):
        print i, lista[i]


def main():
    '''
    Programa Principal
    '''
    N = int(raw_input())
    divInDigits(N)

if __name__ == '__main__':
    main()
