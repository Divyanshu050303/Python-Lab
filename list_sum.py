from functools import reduce

n=[]
num=int(input("Enter the length of list"))
for i in range(num):
    n.append(int(input("Enter the  next number")))
su=reduce(lambda a, b : a+b, n)
print(su)