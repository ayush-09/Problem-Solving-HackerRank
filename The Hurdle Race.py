# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:33:00 2021

@author: ayush
"""

nk = input().split()

n = int(nk[0])
k = int(nk[1])
height = list(map(int, input().rstrip().split()))
a= max(height)- k
if a<=0:
    print(0)
else:
    print(a)