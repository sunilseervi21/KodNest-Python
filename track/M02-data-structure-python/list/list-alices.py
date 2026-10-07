#updating values 
marks=[70,81,60]
stu_marks=marks#passing the same memory reference to stu_marks
stu_marks[0]=100#since both have the same reference one change affects the other
print(marks)
print(stu_marks)


first=[1,2,3]
second=first
print(first is second)#its true because the both are pointing to the same address
print(first==second)#its true because the both have the same value


first=[1,2,3]
second=[1,2,3]
print(first is second)#its false because the both are pointing to the different address
print(first==second)#its true because the both have the same value


#modification
num=[10,20]
values=num
values.append(30)#both gets updated since they point to the same reference
print(num)
print(values)

#reassignment
num=[10,20]
values=num
values=[100,200]
print(num)#num will be same as origianal num
print(values)#values will be values=[100,200] bcoz it will create new memory reference bcoz  lists are mutable

