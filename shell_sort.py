def Shell_Sort(arr):
    n=len(arr)
    gap=n/2
    while gap>0:
        for i in range(gap, n):
            temp=arr[i]
            j=i
            while j>=gap and arr[j-gap]>temp:
                arr[j]=arr[j-gap]
                j-=gap
            arr[j]=temp
        gap/=2


arr=[12, 34, 45, 2, 3]
n=len(arr)
Shell_Sort(arr)
print("Sorting array is :")
for i in range(0, n):
    print(arr[i], end=' ')