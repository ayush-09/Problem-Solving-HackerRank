# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:32:54 2020

@author: ayush
"""
n=int(input())
a=list()
for j in range(n):
    a.append(int(input()))
for i in range(len(a)):
    if(a[i]>37):
        if((a[i]+1)%5==0):
            print(a[i]+1)
        elif((a[i]+2)%5==0):
            print(a[i]+2)
        elif(a[i]%5==0):
            print(a[i])
        else:
            print(a[i])
    else:
        print(a[i])

