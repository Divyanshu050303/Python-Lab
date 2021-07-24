def gnomesort(arr, n):
    index=0
    while index<n:
        if index==0:
            index+=1
        if arr[index]>=arr[index-1]:
            index +=1
        else:
            arr[index], arr[index-1]=arr[index-1], arr[index]
            index-=1
    return arr


arr=[34, 2, 10, -9, -1, 5, 6, 8, -10]
n=len(arr)
arr=gnomesort(arr, n)
print("Sorted array is :")
for i in arr:
    print(i, end=' ')