#noraml code for finding square
square=[]
for i in range(1,6):
    square.append(i*i)
print(square)

#comparision
square=[i*i for i in range(1,6)]
print(square)

#finding even numbers
numbers=[i for i in range(1,11)if i%2==0]
print(numbers)

#findindg numbers greater then 10
numbers=[10,3,12,5,43,7]
new_list=[i for i in numbers if i>10]
print(new_list)

#converting to uppercase
names=["sunil","ravi","manoj","manvith"]
new_list=[name.upper() for name in names]
print(new_list)