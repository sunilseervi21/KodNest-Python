#normal assisgment
Original=[[10,20],[30,40]]
copy1 = Original
copy1[0][0]=100
print(Original)
print(copy1)

#sallow copy
Original=[[10,20],[30,40]]
copy2 = Original.copy()
copy2[0][0]=100
print(Original)
print(copy2)

#deep copy
Original=[[10,20],[30,40]]
import copy
copy3 = copy.deepcopy(Original)
copy3[0][0]=100
print(Original)
print(copy3)