# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 13:33:48 2021

@author: gslee
"""


#10809 
#list형식의 index 사용법 정확히 숙지하기

word = list(input())
for i in range (97,123):
    if chr(i) in word:
        print(str(word.index(chr(i)))+' ',end="")
    else:
        print('-1 ',end="")