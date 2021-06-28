l=int(input())
b=int(input())
a=l*b
p=2*(l+b)
if a>p:
    print("Area")
    print(a)
elif a<p:
    print("Peri")
    print(int(p))
else:
    print("Eq")
    print(a)
