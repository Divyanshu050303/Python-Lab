from array import *
n=list(map(int, input().split()))
a_num=array('i', [])
print("Item in the list", n)
print("append item from the list")
a_num.fromlist(n)
print("Item in the array"+str(a_num))

