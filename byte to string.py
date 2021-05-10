from array import *
print("Byte to string")
a_num=array('b', map(int, input().split()))
b=a_num.tobytes()
print(b)