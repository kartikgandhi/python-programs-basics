x=int(input("Enter the number"))
y=0
for i in range (2,x):
    if(x%i==0):
        y=2
        break;
if(y==0):
    print("prime")
elif(y==2):
    print("not prime")    
