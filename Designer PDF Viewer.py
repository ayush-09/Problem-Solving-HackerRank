# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:47:16 2021

@author: ayush
"""

h = list(map(int, input().rstrip().split()))

word = input()
s='abcdefghijklmnopqrstuvwxyz'
r=[]
n=len(word)
l=list(s)
for i in word:
    if i in l:
        r.append(h[l.index(i)])
print(max(r)*n)
        
    