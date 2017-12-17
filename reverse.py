x=int(input("Enter the number"))
t=1;
s=0;
while(x!=0):
    a=x%10;
    s=a+s*10;
    x=int(x/10)
print(s)
