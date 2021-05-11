n=int(input("Enter the length of dictionary"))
dic={}
for i in range(n):
    key=input(f"Enter the key first")
    value=input("Enter the value ")
    dic[key]=value
print(dic)