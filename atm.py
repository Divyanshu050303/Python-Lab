n=input().split()
a=int(n[0])
b=float(n[1])
c=0.50
if a% 5==0:
    if a<b:
        k=b-a-c
        print(k)
    else:
        print(b)
else:
    print(b)