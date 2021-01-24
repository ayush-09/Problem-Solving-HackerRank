# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 14:40:23 2021

@author: ayush
"""
import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    spec = '!@#$%^&*()-+'
    c=[0,0,0,0]
    for i in password:
        if i.isdigit():
            c[0] =1
        elif i.islower():
            c[1] =1
        elif i.isupper():
            c[2] =1
        elif i in spec:
            c[3] =1
    return max(6-len(password),4-sum(c))
    # Return the minimum number of characters to make the password strong

if __name__ == '__main__':

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    print(str(answer) + '\n')
