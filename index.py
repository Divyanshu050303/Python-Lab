from array import *

val=array('i', [])
n=int(input("Enter the number item in array"))
for i in range(n):
    x=int(input("Enter the next value"))
    val.append(x)
print(val)
m=int(input("Enter the number which index number you require "))
print(val.index(m))
