#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    st='abcdefghijklmnopqrstuvwxyz'
    l=list(st)
    r=''
    for i in s:
        if i.isupper():
            i=i.lower()
            a=l.index(i)
            c= (a+k)%26
            r+=st[c].upper()
        elif i not in l:
            r+=i
            continue
        else:
            a=l.index(i)
            c=(a+k)%26
            r+=st[c]
    return r
if __name__ == '__main__':
    
    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    print(result + '\n')
