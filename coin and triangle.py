for i in range(int(input())):
    l, k = 1, 0
    n = int(input())
    while(n>=l):
        n-=l
        k+=1
        l+=1
    print(k)