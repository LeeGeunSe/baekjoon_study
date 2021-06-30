# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 09:01:27 2021

@author: gslee
"""


#1193
X = int(input())
n=0
pl = 0
while  pl <X:
    n +=1
    pl +=n
left = X-(pl-n)

if n%2 == 1:
    print(str(n-(left-1))+'/'+str(left))
else:
    print(str(left)+'/'+str(n-(left-1)))
    
#2896
A,B,V = map(int,input().split())
total = 0
day = 0
while total<V:
    day +=1
    total += A
    if total<V:
        total -= B
    else:
        print(day)