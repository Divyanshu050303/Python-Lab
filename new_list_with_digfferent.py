def new(lst):
    print(list(set(lst)))


a=[]
n=int(input("Enter the length of list"))
for i in range(n):
    a.append(int(input("Enter the next element")))
new(a)