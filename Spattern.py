for i in range(7):
    for j in range(6):
        if (i%3==0 and (j>0 and j<5)) or (j==0 and (i==1 or i==2)) or (j==5 and (i==4 or i==5)) :
            print("*", end='')
        else:
            print(end=' ')
    print()