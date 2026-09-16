#identity operators
x=[1,2,3]
y=[1,2,3]
print(x==y)
print(x is y)

#membership operators
fruits=["apple","banana","cherry"]
print("banana" in fruits)
print("apple" not in fruits)


text="hllo world"
print("h" in text)
print("hello" in text)
print("z"not in text)

#Ternary operator 
num =15
res="even" if num%2==0 else "odd"
print(res)

#wap to find largest of 3 numbers
a=12
b=4
c=13
largest=a if a>b and a>c else b if  b>c else c
print(largest)

#find positive or negative 
num =5
result="positive" if num >0 else "negative"
print(result)
