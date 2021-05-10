from array import *
n=list(map(int, input().split()))
a_num=array('i', [])
for i in n:
    if i not in a_num:
        a_num.append(i)
print(a_num)