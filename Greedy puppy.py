for _ in range(int(input())):
    n=input().split()
    l=[]
    for i in range(int(n[1]), 0, -1):
        l.append(int(n[0])% i)
    print(max(l))