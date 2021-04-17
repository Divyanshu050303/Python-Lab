m=int(input("Enter the element in the list"))
n=[]
int=[]
f=[]
s=[]
for i in range(m):
    b=input("Enter the element ")
    n.append(b)
print(n)
for i in n:
    if i.isalpha():
        s.append(i)
    elif i.isdigit():
        f.append(i)
    else:
        int.append(i)
print("String in the given list", s)
print("integer in the given list", f)
print("Floating number in the given list", int)
