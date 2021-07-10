for i in range(int(input())):
    a=list(map(str, input().split()))
    b=list(map(str, input().split()))
    c=0
    for j in b:
        if j in a:
            c+=1
    if c>=1:
        print("Similar")
    else:
        print("Dissimilar")