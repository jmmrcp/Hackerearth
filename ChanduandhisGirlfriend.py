# !/usr/bin/python -tt
# -*- coding: utf-8 -*-
'''
Chandu and his Girlfiend
'''


def main():
    numoftest = int(raw_input())

    for n in range(numoftest):
        sizeofArray = int(raw_input())
        array = map(int, raw_input().split())

        arraysorted = sorted(array, reverse=True)
        print " ".join(map(str, arraysorted))

if __name__ == '__main__':
    main()
