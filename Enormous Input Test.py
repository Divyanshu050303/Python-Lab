n=input().split()
a=int(n[1])
c=0
for i in range(int(n[0])):
    m=int(input())
    if m% a==0:
        c+=1
print(c)