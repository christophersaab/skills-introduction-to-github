# -*- coding: utf-8 -*-



#Problem 1  Time
x=int(input("Enter time elapsed: "))
hours=x//3600
y=x-hours*3600
minutes=y//60
seconds=y-minutes*60
print("Converted time ",hours,minutes,seconds,sep=":")