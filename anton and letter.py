n=[]
a=list(input("Enter the list"))
for i in range(0, len(a)):
    if a[i] == '{' or a[i] == ',' or a[i] == '}' or a[i] == ' ':
        pass
    else:
        n.append(a[i])
print(len(set(n)))