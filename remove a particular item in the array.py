from array import *
a_num=array('i', map(int, input("Enter the element").split()))
print("your array : "+str(a_num))
n=int(input("Enter the  element"))
a_num.pop(n)
print(a_num)