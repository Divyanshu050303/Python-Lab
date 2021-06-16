def heapify(array, m, i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<m and array[i]<array[l]:
        largest=l
    if r<m and array[largest]<array[r]:
        largest=r
    if largest!=i:
        array[i], array[largest]=array[largest], array[i]
        heapify(array, m, largest)
def heap_sort(array):
    n=len(array)
    for i in range(n//2, -1, -1):
        heapify(array, n, i)
    for i in range(n-1, 0, -1):
        array[i], array[0]=array[0], array[i]
        heapify(array, i, 0)
    return array


n=list(map(int, input().split()))
print(heap_sort(n))