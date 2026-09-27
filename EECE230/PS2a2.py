#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:07:11 2026

@author: christophersaab
"""

s=input("Enter integers:").split()
L=len(s)*[0]
n=int(input("Enter target integer:"))
for i in range(len(s)):
    L[i]=int(s[i])
print (L)
isin=False
u=0
for j in L:
    if j==n:
        isin=True
        u=u+1
        
if isin:
    print(n,"is in the List ",u," times")
elif not isin:
    print(n,"is not in the list")
    
        
    
    

