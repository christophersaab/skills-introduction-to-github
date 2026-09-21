n=int(input("Enter n:")) 
low=1
high=n
mid=(low+high)//2
square=False
while low<=high:
    if mid*mid==n:
        square=True
        break
    elif mid*mid<n:
        low=mid+1
    elif mid*mid>n:
        high=mid-1
    mid=(low+high)//2
if square:
    print(n,"is a perfect square")
else:
    print(n,"is not a pefect square")
    
    
    

