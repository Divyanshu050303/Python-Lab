e=[]
o=[]
a=[]
b=[]
for i in range(1,101):
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print("Even number list", e)
print("Odd number list",o)
for i in e:
    if i%4==0 or i%6==0 or i%8==0 or i%10==0:
        a.append(i)
for i in o:
    if i%3==0 or i%5==0 or i%7==0 or i%9==0:
        b.append(i)
print("The number divided in even list by 4,6,8,10",a)
print("The number divided  in odd list by 3,5,7,9",b)