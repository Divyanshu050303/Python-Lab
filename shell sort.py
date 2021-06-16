import math


def shell_sort(array):
    m=len(array)
    k=int(math.log2(m))
    interval=2**k-1
    while interval>0:
        for i in range(interval, m):
            temp=array[i]
            j=i
            while j>=interval and array[j-interval]>temp:
                array[j]=array[j-interval]
                j-=interval
            array[j]=temp
        k-=1
        interval=2**k-1
    return array


n=list(map(int, input().split()))
print(shell_sort(n))