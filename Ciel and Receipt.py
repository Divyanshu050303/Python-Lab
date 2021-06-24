m=[2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
for i in range(int(input())):
    p=int(input())
    ans=n=0
    while n<12:
        ans+=p//m[n]
        p=p% m[n]
        if p==0:
            break
        n=n+1
    print(ans)