# !/usr/bin/python -t
# -*- coding: utf-8 -*-
'''
Prateek and his Friends
'''
testCases = int(raw_input())

for case in range(testCases):
    data = map(int, raw_input().split())
    numberFriends, moneytospend = data
    costs = []
    answer = "NO"
    for friend in range(numberFriends):
        cost = int(raw_input())
        costs.append(cost)
        gifts = sum(costs)
        while gifts > moneytospend:
            del costs[0]
            gifts = sum(costs)
        if gifts == moneytospend:
            answer = "YES"
    print answer

