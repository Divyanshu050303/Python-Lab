from array import *
a_num=array('i', map(int, input("Enter the element").split()))
print("your array : "+str(a_num))
n=int(input("Enter the  element"))
m=int(input("Enter number"))
a_num.insert(n, m)
print(a_num)