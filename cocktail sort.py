def cocktailsort(a):
    n=len(a)
    start=0
    end=n-1
    swapped=True
    while swapped==True:

        for i in range(start, end):
            if a[i]>a[i+1]:
                a[i], a[i+1]=a[i+1], a[i]
        if swapped==False:
            break
        swapped=False
        end=end-1
        for j in range(end-1, start-1, -1):
            if a[j]>a[j+1]:
                a[j], a[j+1]=a[j+1], a[j]
                swapped=True
        start+=1


a=[5, 1, 4, 2, 8, 0, 2, 0, 1, 4, 6, 3, 2]
cocktailsort(a)
print("Sorted array is :")
for k in range(len(a)):
    print(a[k], end=' ')