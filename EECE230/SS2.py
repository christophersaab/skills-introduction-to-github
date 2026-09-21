
from math import pi
e=float(input("Enter desired approximation error:"))
s=0
n=0
if e>0:
    while abs((pi**2)/6-s)>=e:
      n=n+1
      s=s+1/n**2
      
    print("The smallet n is",n)
else:
   print("Invalid input")

