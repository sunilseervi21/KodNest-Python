names=('sunil','abhi','sid','abhi')
print(names)
print(type(names))
print(len(names))
print(1,3,4,5,5)
print(names.count('abhi'))
print(names.index('sid'))
print(names[0])
print(names[-1])
print(names[0:3])

#loop
for n in names:
    print(n)

fruits=("sunil",)#comma is required for a single tuble  
print(fruits*3)  

#consturctor
fruits=tuple(("sunil","abhi","sid"))
print(fruits)  

#list in tuple usind constructor
fruits=tuple(["sunil","abhi","sid"])
print(fruits)  

#interview question
#treat as integer
n=10
print(n,type(n))

#treat as tuple
n=(10,)
print(n,type(n))

#deleting the tuple
del fruits


#packing and unpacking 

#unpacking(the process of converting the tuples and breaking them into varibles)
fruits=("apple",'banana','orange')

(f1,f2,f3,)=fruits
print(f1,f2,f3)
print(f1)

num=(1,3,4,5,5)
(n1,*n2)=num
print(n1,n2)
print(type(n2))

#packing(the process of converting the single variales into tubles)
a=10
b=20
c=30
numbers=(a,b,c)
print(numbers,type(numbers))


#joining the tuples
a=(1,2,3)
b=(4,5,6)
c=a+b
print(c,type(c))