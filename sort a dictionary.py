n=int(input("Enter the length of dictionary"))
dic={}
for i in range(n):
    key=input(f"Enter the key first")
    value=input("Enter the value ")
    dic[key]=value
print("The dictionary before sorted", dic)
print("Dictionary after sorted")
for i in sorted(dic):
    print("%s %s"% (i, dic[i]))