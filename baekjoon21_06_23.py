# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 10:03:26 2021

@author: gslee
"""
#1712
A,B,C = map(int, input().split())
if B>=C: #크다고만 표시할 경우 아래 나눠주는값이 0이 되어 런타임에러중 ZerodivisionError 발생할 수 있음
    print('-1')
else:
    print(int(A/(C-B)+1))

#2292
n= int(input())
layer=1
start=1
while start<n:
    start+=layer*6
    layer+=1
print(layer)
