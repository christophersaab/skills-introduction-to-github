n=int(input("Enter an integer n:"))
i=1
square=False
if n==0:
    print("YES square",n,"=0^2")
elif n<0:
    print("n cannot be negative")
else:
    for i in range(1,n):
        if i*i==n:
            square=True
            break
    if  square:
        print("YES square:",n,"=",i,"^2")





    
    
   
        
    



