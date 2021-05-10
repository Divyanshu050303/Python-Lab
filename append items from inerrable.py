from array import *
a_num=array('i', map(int, input().split()))
print("Original"+str(a_num))
a_num.extend(a_num)
print("After the extended "+str(a_num))