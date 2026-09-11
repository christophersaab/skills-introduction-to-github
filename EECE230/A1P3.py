#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 17:05:38 2026

@author: christophersaab
"""
from math import sqrt
a=float(input("Enter \"a\":"))   
b=float(input("Enter \"b\":"))
c=float(input("Enter \"c\":"))
if a!=0:
    d=b*b-4*a*c
    if d>0:
        x1=(-b+sqrt(d))/(2*a)
        x2=(-b-sqrt(d))/(2*a)
        print(f"The equation has two roots :{x1} and {x2}")
    elif abs(d)<1e-9:
            x=(-b/2*a)
            print(f"The equation has one root: {x}")
    else:
                print("The equation has no roots")
else:
    print("\"a\" can\'t be equal to \"0\"")
    
    