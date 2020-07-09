import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # put words into alphabetical order
    magazine.sort()
    note.sort()
    # starting index
    m = 0
    n = 0
    count = 0
    # loop through each
    while m < len(magazine) and n < len(note):
        # if words match
        if magazine[m] == note[n]:
            # add to count & move to next index(word)
            count += 1
            n += 1
        # move to next word in magazine
        m += 1
    
    if count == len(note):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
