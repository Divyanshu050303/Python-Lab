def selection_sort(array):
    for i in range(len(array)):
        k=i
        for j in range(i+1, len(array)):
            if array[j]<array[k]:
                k=j
        array[i], array[k]=array[k], array[i]
    return array


n=list(map(int, input().split()))
print(selection_sort(n))