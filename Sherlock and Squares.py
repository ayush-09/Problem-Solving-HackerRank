# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:09:22 2020

@author: ayush
"""

import math
import os
import random
import re
import sys
from math import *
# Complete the squares function below.
def squares(a, b):
    f=floor(sqrt(b))
    c=ceil(sqrt(a))
    return (f-c)+1
if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        print(result)