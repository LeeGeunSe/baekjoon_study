# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 17:29:21 2021

@author: gslee
"""

#1152
para = list(input().split())
print(len(para))

#2908
A,B = map(str,input().split())
New_A = int(A[::-1])#거꾸로 쓰는 방법 기억하기
New_B = int(B[::-1])#거꾸로 쓰는 방법 기억하기
if New_A>New_B:
    print(New_A)
else:
    print(New_B)
    
#5622  아스키코드 사용하기
A_list=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = list(input())
time = 0
for i in range(len(word)):
    for j in range(len(A_list)):
        if word[i] in A_list[j]:
            time += j+3
print(time)

#2941 크로아티아 알파벳
A_list=['c=','c-','dz=','d-','lj','nj','s=','z=']
w = input()
for t in A_list:
    w = w.replace(t,'0')
print(len(w))

#1316 알고리즘 공부 중요
num = input()
final=0
for j in range (int(num)):
    check =0
    word = input()
    for i in range(len(word)-1):
        if word[i]!=word[i+1]:
            if word[i] in word[i+1:]:
                check += 1
    if check == 0:
        final +=1
print(final)
