#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 17:15:01 2026

@author: christophersaab
"""

x=int(input("Enter x: "))
d=2
IsPrime=True
if n<=1:
    print(n,"is not prime")
else:
    while d*d<=x:
        if x%d==0:
            IsPrime=False
            print("x is not a prime")
            break
    d=d+1
    if IsPrime:
        print("x is prime")
    
