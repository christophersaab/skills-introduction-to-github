#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:19:42 2026

@author: christophersaab
"""

L=[int(n) for n in input("Enter a sequence of integers:").split()]
x=int(input("Enter target integer:"))
sum=False
P=[]
for i in range(len(L)-1):
    for j in range(i+1,len(L)):
        if x==L[i]+L[j]:
            sum=True
            P.append([L[i],L[j]])
            
print(P)
if sum:
    print("The pairs are:")
    for u in P:
        print(u)
if not sum:
    print("no match")
            
