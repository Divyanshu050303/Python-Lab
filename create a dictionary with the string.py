
n=input("Enter the string")
dic={}
for i in n:
    dic[i]=dic.get(i, 0)+1
print(dic)