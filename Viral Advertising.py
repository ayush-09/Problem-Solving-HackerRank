# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 20:45:09 2021

@author: ayush
"""
n = int(input())
t_likes = 0
shared=5
for i in range(n):
    like = shared//2
    t_likes += like
    shared = like * 3
print(t_likes)