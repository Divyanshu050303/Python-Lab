def sort(num):
    for i in range(len(num)):
        minpos=i
        for j in range(i,len(num)):
            if num[j]<num[minpos]:
                minpos=j
        temp=num[i]
        num[i]=num[minpos]
        num[minpos]=temp


num=list(map(int, input().split()))
sort(num)
print(num)