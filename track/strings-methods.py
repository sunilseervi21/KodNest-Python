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
print("count('o'):",s.count("o"))
print("find('Tech'):",s.find("Tech'"))

#replace
print("replace('123','2025'):",s.replace("123","2025"))

#start & end check
print("startswith(' Kod'):",s.startswith(" Kod"))
print("endswith('123  '):",s.endswith("123  "))

#split & join
words=s.split()
print("split():",words)
print("join():","".join(words))


#srtrip spaces
print("strip():",s.strip())
print("lstrip():",s.lstrip())
print("rstrip():",s.rstrip())


#checking methods
print("isalnum():",s.isalnum())
print("isalpha():",s.isalpha())
print("isdigit():",s.isdigit())
print("islower():",s.islower())
print("isupper():",s.isupper())
print("istitle():",s.istitle())
print("isspace():",s.isspace())

#length
print("length of the string:", len(s))