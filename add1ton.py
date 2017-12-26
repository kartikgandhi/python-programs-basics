def add(a):
    sum=0
    for i in range (1,a+1):
        sum=sum+i
    return sum

a=int(input("Enter number "))
print ("sum till ",a," is ",add(a))        
