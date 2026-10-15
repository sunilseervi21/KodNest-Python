#cube number 
numbers=[2,3,4,5]
cube_by_number={}
for number in numbers:
    cube_by_number[number]=number*number*number
print(cube_by_number)

#using dict comprehension
dict_comp={number:number*number*number for number in numbers}
print(dict_comp)