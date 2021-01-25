# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:51:19 2021

@author: ayush
"""

ranked_count = int(input().strip())

ranked = list(map(int, input().rstrip().split()))

player_count = int(input().strip())

player = list(map(int, input().rstrip().split()))

ranked = list(set(ranked))
ranked.sort()
n= len(ranked)
i = 0
r=[]
for j in player:
    while i<n and ranked[i]<=j:
        i+=1
    r.append(n-i+1)
print(r)
