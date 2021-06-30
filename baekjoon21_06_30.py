# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 17:17:36 2021

@author: gslee
"""
#2869
day,night,goal = map(int, input().split())
n=0
reach=0
while reach<goal:
    reach += day
    n+=1
    if reach<goal:
        reach-=night
print(n)

#2869 better way efficiency
day,night,goal = map(int, input().split())
if (goal-day)%(day-night)>0:
    ans = (goal-day)//(day-night)+1+1
else:
    ans = (goal-day)//(day-night)+1
print(ans)