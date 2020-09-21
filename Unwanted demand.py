# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 17:02:28 2020

@author: ayush
"""
a=[]

n=int(input())
for i in range(n):
    a.append(int(input()))
s=int(input())
i=0
c=0
a.sort()
while(s>0):
    s-=a[i]
    if(s>=0):
        c+=1
    i+=1
    if(i>len(a)-1):
        break
print(c)
