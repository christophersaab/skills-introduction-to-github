x=int(input("Enter x: "))
if x<0:
     print("Negative number")
elif x==0:
     print("cannot input 0")
else:
    y=0
    for i in range (2,x+1):
        isprime=True
        d=2
        while d*d<=i:
            if i%d==0:
                isprime=False
                break
        d=d+1
    if isprime:
            y=y+1
print(y/x)

