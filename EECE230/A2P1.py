#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 14:44:08 2026

@author: christophersaab
"""

n=int(input("Enter an integer n: "))
if n>0:
    s=1
    for i in range (1,n+1):
        s=s*i
    print("Factorial of n:",s)
else:
    if n==0:
        print("Factorial of n=1 ")
    else:
        print("Negative number!")
