import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    prices = {}

    for i, p in enumerate(cost, 1):
        n = money - p

        if n in prices:
            print(prices[n], i)
        else:
            prices[p] = i
            
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)