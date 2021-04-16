def person(name, **data):
     print(name)
     for i, j in data.items():
        
         print(i,"->", j)
m=input("Enter the name")
a=int(input("Enter your age"))
s=input("Enter the state")
p=int(input("Enter your phone munber"))
person(name=m , age=a, state=s, mob=p)
