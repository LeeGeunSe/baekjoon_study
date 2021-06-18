# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 14:06:33 2021

@author: gslee
"""

#2675

#코드 간단하게 만드는 연습

num = int(input())
for j in range (num):
    cyc,ch = input().split()    
    for i in range(len(ch)):
        print(ch[i]*int(cyc),end="")
    print("")



