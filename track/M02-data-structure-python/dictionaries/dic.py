#dictionaries are in key vlaue pairs, they are mutable , key cannot be duplicate but value can be
Student={
    "name":"Amit",
    "age":21,
    "course":"Computer Science",
    "Tech":["computer Science", "python","sql"]
}
#accessing values 
print(Student["name"])
print(Student["Tech"])
print(Student["Tech"][0])

#update values or modify values
Student["age"]=22
print(Student)

#adding the new key pair in dictionaries
Student.update({'cgpa':8.4})
print(Student)

#access all the keys
print(Student.keys())

#access all the values
print(Student.values())

#access all the key value pairs
print(Student.items())

#get method
print(Student.get("name"))

#remove items from the dictionary
Student.pop("age")
print(Student)

#remove last item from the dictionary
Student.popitem()
print(Student)

#remove all the items from the dictionary
Student.clear()
print(Student)

student1={
    "name":"rahul",
    "tech":["python","sql"]
}
student1.setdefault("age",22)#used when you dont declare value or key
print(student1)

keys=["name","age","course"]
student1=dict.fromkeys(keys,"hiiii")
print(student1)


#copy
my_dict=student1.copy()
print(my_dict)
my_dict.update({'name':"sunil"})
print(my_dict)



#looping in dictionaries
student2={
    "name":"Rahul",
    "language":"java",
    "marks":88
}

for x in student2:
    print(x)#it just prints all the keys one by one

for x in student2:
    print(student2[x])#it prints all the vlaues one by one

for x in student2:
    print(f"{x}=>{student2[x]}")#print both the keys and vlaues

for x in student2.items():
    print(x)    
    




