x=int(input("Enter x: "))
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

