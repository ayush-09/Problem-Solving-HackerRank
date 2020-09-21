# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 17:09:07 2020

@author: ayush
"""
def minimumBribes(q):
    c=0
    for i in range((len(q)-1),0,-1):
        if(q[i]!=i+1):
            if(q[i-1]==i+1):
                c+=1
                q[i-1],q[i]=q[i],q[i-1]
            elif(q[i-2]==i+1):
                c+=2
                q[i-2],q[i-1]=q[i-1],q[i-2]
                q[i-1],q[i]=q[i],q[i-1]
            else:
                print("Too chaotic")
                return
    print(c)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
