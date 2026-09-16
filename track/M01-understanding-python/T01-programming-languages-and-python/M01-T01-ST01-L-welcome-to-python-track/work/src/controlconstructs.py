#if statement
age=int(input("enter your age"))
if age>18:
    print("eligible for vote")

#if-else statement
age=int(input("enter your age"))
if age>18:
    print("eligible for vote")
else:
    print("not eligible for vote")       

#elif statement
marks=int(input("enter your marks"))
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
elif marks>=60:
    print("Grade D")
else:
    print("Fail")     

#nested if
age1=int(input("enter your age"))    
age2=int(input("enter your age"))    
if age1>=18:
    if age2<=70:
        print("eligible for vote")
    else:
        print("not eligible for vote")
else:
    print("not eligible for vote")        


#match statement
day=3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")


























