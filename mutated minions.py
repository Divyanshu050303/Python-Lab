for i in range(int(input())):
    n=input().split()
    m=list(map(int, input().split()))
    c=0
    for j in range(len(m)):
        k=m[j]+int(n[1])
        if k% 7==0:
            c+=1
    print(c)