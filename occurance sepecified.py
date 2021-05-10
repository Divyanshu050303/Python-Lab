from array import *
a_num=array('i', map(int, input().split()))
print("Original"+str(a_num))
m=int(input("Enter the number which you want to fin there occurrence"))
print(f"Number of occurrences of the number {m} in the said array: "+str(a_num.count(m)))
