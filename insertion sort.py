def insertion_sort(array):
    for i in range(1, len(array)):
        k=array[i]
        j=i-1
        while array[j]>k and j>=0:
            array[j+1]=array[j]
            j-=1
        array[j+1]=k
    return array


n=list(map(int, input().split()))
print(insertion_sort(n)[::-1])