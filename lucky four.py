for i in range(int(input())):
    n=input()
    c=0
    for j in range(len(n)):
        if n[j]=='4':
            c+=1
    print(c)