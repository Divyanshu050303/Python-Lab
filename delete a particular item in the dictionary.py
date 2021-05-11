n=int(input("Enter the length of dictionary"))
dic={}
for i in range(n):
    key=input(f"Enter the key first")
    value=input("Enter the value ")
    dic[key]=value
print(dic)
m=input("Enter the item which you want to delete")
if m in dic:
    del dic[m]
    print("After the delete your item ", dic)
else:
    print("You enter invalid choose")