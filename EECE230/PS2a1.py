#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 13:17:11 2026

@author: christophersaab
"""

L=[int(x) for x in (input("Enter integers:").split())]
a=int(input("Enter a number"))
u=0
isinlist=False
for n in L:
    if a==n:
        u+=1
    isinlist==True
    
if isinlist:
    print(a,"is in the list",u,"times")
else:
    print(a,"is not in the list")
        
        