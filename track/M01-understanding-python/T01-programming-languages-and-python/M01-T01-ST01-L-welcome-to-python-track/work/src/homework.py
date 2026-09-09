#swap two number without using the third variable
a=10
b=20
b=a+b
a=b-a
b=b-a
print("a=",a,"b=",b)

#check if is a prime number or not
n=4
for i in range(2,n):
    if(n%i==0):
        print("not a prime")
        break
else:
     print("its a prime number")    

#fibonacci series 
a = 0
b = 1

for i in range(4):
    print(a, end=" ")
    sum=a+b
    a=b
    b=sum