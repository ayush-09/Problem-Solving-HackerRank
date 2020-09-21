# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:55:03 2020

@author: ayush
"""

n=int(input())

def daydetect(a,l,f):
    s=0
    i=0
    while s<256:
        temp1=l[i] if f else a[i]
        s+=temp1
        temp=s
        temp+=temp1
        if(temp>256):
            break
        i+=1
    i+=1
    d=256-s
    i+=(0 if d==0 else 1)
    z="0"+str(i) if (i<10) else i
    print(str(d)+"."+str(z)+"."+str(n))
a=[31,28,31,30,31,30,31,31,30,31,30,31]
l=[31,29,31,30,31,30,31,31,30,31,30,31]
if 1700<=n<=1917:
    f=bool((n%4==0))
    daydetect(a, l, f)
elif 1919<=n<=2700:
    f=bool((n%400==0)or((n%4==0)and (n%100!=0)))
    daydetect(a, l, f)
elif(n==1918):
    s=0
    i=0
    a=[31,16,31,30,31,30,31,31,30,31,30,31]
    while s<256:
        temp1=a[i]
        s+=temp1
        temp=s
        temp+=temp1
        if(temp>256):
            break
        i+=1
    i+=1
    d=256-s
    i+=(0 if d==0 else 1)
    z="0"+str(i) if (i<10) else i
    print(str(d+1)+"."+str(z)+"."+str(n))
