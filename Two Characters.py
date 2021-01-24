# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 15:40:29 2021

@author: ayush
"""

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    m=c=0
    a=list(set(s))
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            l=[a[i],a[j]]
            if s.index(a[i])<s.index(a[j]):
                ind = 0
            else:
                ind = 1
            for cha in s:
                if cha in l:
                    if cha==l[ind]:
                        c+=1
                        ind = ind ^ 1
                    else:
                        c=0
                        break
            m = max(m,c)
            c=0
    return m
            

if __name__ == '__main__':

    l = int(input().strip())

    s = input()

    result = alternate(s)

    print(str(result) + '\n')