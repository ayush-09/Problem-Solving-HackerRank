# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 20:07:10 2021

@author: ayush
"""
ijk = input().split()

i = int(ijk[0])

j = int(ijk[1])

k = int(ijk[2])

c = 0

for i in range(i, j+1):
    s = str(i)
    re = int(s[::-1])
    d = abs(i-re)
    if d % k == 0:
        c += 1
print(c)
    