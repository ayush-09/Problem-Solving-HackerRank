# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:53:46 2021

@author: ayush
"""
t=int(input())
for i in range(t):
    
    n = int(input())
    c=0
    for i in range(0,n+1):
        if i%2==0:
            c+=1
        else:
            c=c*2
    print(c)
            