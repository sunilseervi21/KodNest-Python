#inbuilt string methods
s="  Kodnest Technologies 123"
print("Original string:",s)

#case  conversion methods
print("upper():",s.upper())#KODNEST TECHNOLOGIES 123
print("lower():",s.lower())#  kodnest technologies 123
print("title():",s.title())#  Kodnest Technologies 123
print("swapcase():",s.swapcase())#  kODNEST tECHNOLOGIES 123
print("capitalize():",s.capitalize())#  kodnest technologies 123  

#counting methods
print("count('o'):",s.count("o"))#3
print("find('Tech'):",s.find("Tech'"))#11

#replace
print("replace('123','2025'):",s.replace("123","2025"))#  Kodnest Technologies 2025

#start & end check
print("startswith(' Kod'):",s.startswith(" Kod"))#true
print("endswith('123  '):",s.endswith("123  "))#true

#split & join
words=s.split()
print("split():",words) #['Kodnest', 'Technologies', '123']
print("join():","".join(words)) #KodnestTechnologies123


#srtrip spaces
print("strip():",s.strip())#['Kodnest', 'Technologies', '123']
print("lstrip():",s.lstrip())#Kodnest Technologies 123  
print("rstrip():",s.rstrip())#  Kodnest Technologies 123


#checking methods
print("isalnum():",s.isalnum())#false
print("isalpha():",s.isalpha())#false
print("isdigit():",s.isdigit())#false
print("islower():",s.islower())#false
print("isupper():",s.isupper())#false
print("istitle():",s.istitle())#true
print("isspace():",s.isspace())#false

#length
print("length of the string:", len(s))#29

s1="hello"
print(id(s1))
print(s1)
s1=s1+"world"
print(s1)
print(id(s1))

s1="hello"
s2=s1+"world"
print(id(s1),s1)
print(id(s2),s2)

s1="python"
s2="python"
print(id(s1),s1)
print(id(s2),s2)
print(s1==s2)
print(s1 is s2)