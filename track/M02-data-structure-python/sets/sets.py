#stes are unordered,unindexed,unchangable,duplicate not allowed,mutable
s={1,2,3,4,5}
print(s)
#print(s[1])#sets does not support indexing and slicing

s.add(10)
print(s)

s.update({8, 4})#adds multiple values
print(s)

s.remove(10)#removes the specified value
print(s)

s.discard(8)#removes the specified value and does not show error
print(s)

s.pop()
#s.clear()#makes set empty
print(s)

#del s #deletes the set

s1={1,2,3,"hello",1.2,True,0,1}#prints in unordered
print(s1)

#constructor of sets
s2=set()
print(s2,type(s2))
s3=set([1,2,3,4])#constructor of sets with list
print(s3,type(s3))
#loop
for n in s3:
    print(n)

#frozensets-immutable
fs= frozenset([1,2,3])
print(fs,type(fs))    


