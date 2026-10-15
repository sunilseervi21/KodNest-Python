cities=["Bengaluru","Pune","bengaluru","Chennai","Pune"]
u_cities={city.lower() for city in cities}#this coverts list into set then all upper case to lower and then remove dulplicates
print(u_cities)

#printing only the squares of the unique numbers using normal code
numbers=[2,3,2,4,3]
unique_numbers=set()
for number in numbers:
    unique_numbers.add(number*number)
print(unique_numbers)

#printing the square only using set comprehension
set_comp={number*number for number in numbers}
print(set_comp)

