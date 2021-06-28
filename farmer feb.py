for i in range(int(input())):
    n, m=map(int, input().split())
    l=[]
    p=m+n
    k=p+1
    while True:
        l=0
        for j in range(2, k):
            if k% j==0:
                l=1
                break
        if l==1:
            k+=1
        else:
            break
    print(k-p)