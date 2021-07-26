def countingSort(arr, exp1):
    n=len(arr)
    out=[0]*n
    count=[0]*10
    for i in range(0, n):
        index=arr[i]/exp1
        count[int(index% 10)]+=1
    for i in range(1, 10):
        count[i]+=count[i-1]
    i=n-1
    while i>=0:
        index=arr[i]/exp1
        out[count[int(index% 10)]-1]=arr[i]
        count[int(index% 10)]-=1
        i-=1
    for i in range(0, len(arr)):
        arr[i]=out[i]


def radixSort(arr):
    max1=max(arr)
    exp=1
    while max1/exp:
        countingSort(arr, exp)
        exp*=10


arr=[170, 45, 75, 96, 802, 24, 2, 66]
radixSort(arr)
for i in range(len(arr)):
    print(arr[i], end=' ')