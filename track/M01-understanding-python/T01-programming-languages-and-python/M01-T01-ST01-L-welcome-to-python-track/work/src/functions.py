#function first program
def sum():
    a,b=10,20
    c=a+b
    print(c)

sum()   

#largest of three number
def lar():
    a,b,c=20,30,50
    if(a>b and a>c):
        print(a)
    elif(b>a and b>c):
        print(b)
    else:
        print(c)

lar()

#no agruments +no return value
def sum():
    a,b=10,20
    c=a+b
    print(c)
sum()
#no arguments + with return value
def sum():
    a,b=10,20
    c=a+b
    return c
print(sum()) 

#with arguments + no return value
def sum(a,b):
    c=a+b
    print(c)    
sum(2,5) 

#with arguments + with return value
def sum(a,b):
    c=a+b
    return c
print(sum(4,8)) 

#important
def sum(a,b):
    return a+b,a-b
add,diff=sum(100,50)
print(add,diff)
