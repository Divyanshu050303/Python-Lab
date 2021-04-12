for i in range(7):
    for j in range(6):
        if i==0 or (j==5 and (i==1 or i==2 or i==3)) or (i==4 and j==5) or (i==5 and (j==5 or j==1)) or (i==6 and (j==2 or j==4)):
            print("*",end='')
        else:
            print(end=' ')
    print()