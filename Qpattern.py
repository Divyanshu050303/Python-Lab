for i in range(6):
    for j in range(5):
        if (i==0 and (j==1 or j==2 or j==3) or ( i==1 and (j==0 or j==4)) or ( i==4 and  j==3)or  (i==5 and (j==1 or j==2 or j==4)) or (i==3 and j==2) or (j==0 and (i==2 or i==3 or i==4)) or (j==4 and (i==2 or i==3))):
            print("*", end='')
        else:
            print(end=' ')
    print()