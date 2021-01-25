# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 17:29:12 2021

@author: ayush
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    c=0
    for i in range(len(a)):
        if a[i]<=0:
            c+=1
    if c>=k:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        print(result + '\n')