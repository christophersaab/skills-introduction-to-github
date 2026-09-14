#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 14:51:36 2026

@author: christophersaab
"""

n=int(input("Enter an integer n:"))
if n>0:
    i=1
    s=1
    while i<=n:
        s=s*i
        i=i+1
    print("Factorial of n: ",s)
else:
    if n==0:
        print("Factorial of n: 1")
    else:
        print("Negative number!")
        