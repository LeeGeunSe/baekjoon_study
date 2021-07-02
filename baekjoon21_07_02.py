# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:31:04 2021

@author: gslee
"""

#10250
Q= int(input())
for i in range(Q):
    H,W,n = map(int,input().split())
    if n%H ==0:
        print(str(H)+str('%02d'%(n//H)))# 맨 꼭대기층
    else:
        print(str(n%H)+str('%02d'%(n//H+1)))