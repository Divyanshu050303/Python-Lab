n=int(input("Enter the length of dictionary"))
dic={}
for i in range(n):
    key=input(f"Enter the key first")
    value=input("Enter the value ")
    dic[key]=value
print("Original dictionary", dic)
key_max=max(dic.keys(), key=(lambda k: dic[k]))
key_min=min(dic.keys(), key=(lambda k: dic[k]))
print("Maximum in the dictionary:", key_max)
print("Minimum in the dictionary:", key_min)