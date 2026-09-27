#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 13:49:20 2026

@author: christophersaab
"""
L=[int(x)for x in input("Enter integers:").split()]
n=int(input("Input n"))
if n in L:
    print(n,"is in list")
elif not(n in L):
    print(n,"is not in List")