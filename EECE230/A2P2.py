n=int(input("Enter number n of integers:"))
if n==0:
    print("n cannot be 0")
else:
    maximum=int(input("Enter an integer:"))
    i=1
    while i<n:
        i=i+1
        x=int(input("Enter an integer:"))
        if x>maximum:
            maximum=x
      
print(maximum,i)